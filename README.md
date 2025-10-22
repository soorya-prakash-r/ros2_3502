# 🎲 ROS 2 Dice Roller

A fun ROS 2 Python project that simulates a virtual dice.  
The node publishes a random dice number (1–6) every 2 seconds on a ROS 2 topic.  
Other nodes can subscribe to this topic to trigger actions based on the dice roll.

---

## 🧠 Features
- Publishes a random dice number (1–6) every 2 seconds  
- Interactive and can be subscribed to by other ROS 2 nodes  

---

## 🚀 How to Run
```bash
# 1. Clone the repository into your ROS 2 workspace
cd ~/ros2_ws/src
git clone https://github.com/soorya-prakash-r/ros2_3502.git

# 2. Build the workspace
cd ~/ros2_ws
colcon build
source install/setup.bash

# 3. Run the dice roller node
ros2 run dice_roller dice_roller
