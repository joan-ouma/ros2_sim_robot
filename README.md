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
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
*Note: Ensure your terminal is focused to send keyboard commands to the robot.*

---

## 🗺️ Running SLAM (Mapping)

This package is fully configured to generate 2D maps of the environment using LiDAR and Odometry data via the `slam_toolbox`.

1. **Launch the Simulation:** (As described above in step 2)
2. **Start the SLAM Node:** In a **new terminal**, launch the SLAM toolbox with the custom configuration parameters:
   ```bash
   source ~/Desktop/ros2_sim_robot/robot2_ws/install/setup.bash
   ros2 launch my_robot slam.launch.py
   ```
3. **Open RViz2:** In a **third terminal**, run `rviz2` to visualize the mapping process.
   * Change the **Fixed Frame** to `map`.
   * Add the **Map** display and set the topic to `/map`.
   * Add the **LaserScan** display and set the topic to `/scan` to see the live LiDAR rays.
4. **Map the Environment:** Drive the robot around the gamefield using the `teleop_twist_keyboard` terminal until the entire area is discovered.
5. **Save the Map:** Once satisfied with the map, save it using the `nav2_map_server`:
   ```bash
   ros2 run nav2_map_server map_saver_cli -f my_competition_map
   ```

For a deeper dive into how SLAM works in this project, check out the included [Beginner's Guide to SLAM](slam.md) file!
