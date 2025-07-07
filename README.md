# ROS 2 Waypoint Navigation with TurtleBot3

#DEMO#
Watch the demo video on YouTube: https://youtu.be/lvlVEm0qk1U

This project demonstrates autonomous waypoint navigation using ROS 2, TurtleBot3, and Gazebo. The robot operates in a simulated environment, following a sequence of predefined waypoints using the Nav2 stack and LiDAR-based obstacle avoidance.

Package: `robot_nav`



Features

- Waypoint following with Nav2
- LiDAR-based obstacle detection
- TurtleBot3 simulation in Gazebo
  
Ensure you have:

- ROS 2 (Humble)
- `turtlebot3_gazebo`
- `nav2_bringup`
- Gazebo 11 or compatible
- TurtleBot3 model set to `burger` (default)
- A properly sourced ROS 2 workspace (`~/ros2_ws`)

1. 
```bash
cd ~/ros2_ws/src
git clone https://github.com/SnipyStudy/ros2-waypoint-navigation.git
mv ros2-waypoint-navigation/robot_nav ./
rm -rf ros2-waypoint-navigation

2. cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

Terminal 1: export TURTLEBOT3_MODEL=burger
source ~/ros2_ws/install/setup.bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

Terminal 2: export TURTLEBOT3_MODEL=burger
source ~/ros2_ws/install/setup.bash
ros2 launch nav2_bringup bringup_launch.py use_sim_time:=true

Terminal 3: source ~/ros2_ws/install/setup.bash
ros2 run robot_nav waypoint_navigator
