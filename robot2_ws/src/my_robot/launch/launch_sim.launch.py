import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, AppendEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    package_name='my_robot'

    dk = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','dk.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )
    
    world = LaunchConfiguration('world')

    # Explicitly build the full path to your world file inside the package
    default_world_path = os.path.join(
        get_package_share_directory(package_name),
        'worlds',
        'competition.sdf'
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value=default_world_path,
        description='Full path to world file to load'
        )
        
    # Tell Gazebo exactly where to find your custom gamefield model!
    set_env_vars_resources = AppendEnvironmentVariable(
            'GZ_SIM_RESOURCE_PATH',
            os.path.join(get_package_share_directory(package_name), 'worlds', 'models')
            )

    # Include the Gazebo launch file, provided by the ros_gz_sim package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]),
                    launch_arguments={'gz_args': ['-r -v4 ', world], 'on_exit_shutdown': 'true'}.items()
             )

    # Run the spawner node from the ros_gz_sim package.
    spawn_entity = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-name', 'my_robot',
                                   '-z', '0.5'],
                        output='screen')
              
    # Launch the ROS-gazebo bridge for normal topics
    bridge_params = os.path.join(get_package_share_directory(package_name),'config','gz_bridge.yaml')
    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ]
    )

    # Launch them all!
    return LaunchDescription([
        dk,
        world_arg,
        set_env_vars_resources,
        gazebo,
        spawn_entity,
        ros_gz_bridge,
    ])
