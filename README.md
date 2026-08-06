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

