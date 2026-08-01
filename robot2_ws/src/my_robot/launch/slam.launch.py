import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    my_robot_dir = get_package_share_directory('my_robot')
    
    # Path to our custom config file
    slam_config_file = os.path.join(my_robot_dir, 'config', 'mapper_params_online_async.yaml')

    return LaunchDescription([
    ])
