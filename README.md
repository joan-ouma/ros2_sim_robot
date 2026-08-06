# ROS 2 Robot Simulation (`my_robot`)

A complete ROS 2 package featuring a differential-drive robot simulated in modern Gazebo Sim. This project includes a customized competition gamefield environment, ROS-Gazebo parameter bridging, and full SLAM (Simultaneous Localization and Mapping) capabilities out of the box.

---

## 🌟 Key Features

* **Gazebo Sim Integration:** Fully configured for the modern Gazebo simulation environment using `ros_gz_sim` and `ros_gz_bridge`.
* **Custom Competition Gamefield:** Includes a pre-configured `competition.sdf` world featuring the "auracle" gamefield model with tuned collision geometry to prevent physical clipping.
* **ROS-Gazebo Parameter Bridge:** Real-time bidirectional translation between Gazebo Sim and ROS 2 for odometry, transformations, and control topics.
* **SLAM Ready:** Comes with a pre-configured `slam_toolbox` setup for online asynchronous mapping, allowing the robot to build detailed 2D maps of the competition field using simulated LiDAR.

---

## 🛠️ Prerequisites

Ensure you have the required ROS 2 packages and Gazebo simulation drivers installed:

```bash
sudo apt update
sudo apt install ros-$ROS_DISTRO-ros-gz-sim ros-$ROS_DISTRO-ros-gz-bridge ros-$ROS_DISTRO-teleop-twist-keyboard ros-$ROS_DISTRO-slam-toolbox
```

---

## 🚀 Running the Simulation

Follow these steps to launch the robot in the Gazebo simulator and drive it around.

### 1. Build the Workspace

Open a terminal and navigate to your workspace directory to compile the package:

```bash
cd ~/Desktop/ros2_sim_robot/robot2_ws
colcon build --symlink-install
```

### 2. Launch the Simulation Environment

Source your workspace and launch the main simulation file. This will open Gazebo, spawn the competition world, and place `my_robot` into the environment.

```bash
source install/setup.bash
ros2 launch my_robot launch_sim.launch.py
```

### 3. Drive the Robot (Teleop)

In a **second terminal**, run the teleop node to control the robot with your keyboard:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
