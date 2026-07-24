# ROS 2 4WD Rover Simulation (`my_robot`)

A complete ROS 2 package featuring a 4-wheel drive (4WD) differential-steer rover simulated in modern Gazebo Sim. This project implements custom Xacro inertia macros, GPU-accelerated raycasting LiDAR, real-time ROS 2 parameter bridging, and hardware control configurations.

---

## Key Features

* **4WD Skid-Steer Kinematics:** Uses Gazebo's modern `DiffDrive` system plugin with synchronized dual-motor mapping per side (`front_left` + `back_left` and `front_right` + `back_right`) to achieve 4-wheel skid-steer navigation.
* **GPU-Accelerated LiDAR (`laser_frame`):** Simulates a 360-degree laser scanner (0.3m to 12.0m range) using Gazebo's `gpu_lidar` and `gz-sim-sensors-system` engines, publishing cleanly to `/scan`.
* **ROS-Gazebo Parameter Bridge:** Bidirectional real-time translation between Gazebo Sim (`gz.msgs`) and ROS 2 DDS (`ros_msgs`) for odometry (`/odom`), transformations (`/tf`), joint states (`/joint_states`), and driving commands (`/cmd_vel`).
* **Accurate Physics & Collisions:** Tuned gamefield geometry utilizing static STL meshes to ensure perfect physical barriers and prevent robot clipping during simulation.
* **Physical Hardware Readiness:** Includes official `ros2_control` configurations (`my_controllers.yaml`) and persistent serial device launching for real-world Slamtec RPLIDAR hardware (`rplidar.launch.py`).
---

## Prerequisites

Make sure you have the following ROS 2 packages and simulation drivers installed:

```bash
sudo apt update
sudo apt install ros-$ROS_DISTRO-ros-gz-sim ros-$ROS_DISTRO-ros-gz-bridge ros-$ROS_DISTRO-teleop-twist-keyboard
