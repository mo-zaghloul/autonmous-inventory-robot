## Project Plan: Autonomous Inventory Robot (Simulation → Hardware)

### **Phase 1 — Environment Setup** 
- Install ROS2 (Humble or Jazzy) + Gazebo
- Set up  workspace structure properly (`src/`, `launch/`, `config/`, etc.)
- Create robot package with best practices

### **Phase 2 — Robot Modeling (URDF/Xacro)**
- Model a simple differential-drive robot in URDF
- Add LiDAR sensor to the model
- Visualize it in RViz2 to confirm it looks right

### **Phase 3 — Simulation in Gazebo**
- Spawn robot in a simulated warehouse/shelf environment
- Confirm LiDAR scan data is publishing correctly
- Drive it around manually to sanity-check physics

### **Phase 4 — Mapping**
- Run **SLAM Toolbox** to build a 2D map of the simulated environment
- Save the map

### **Phase 5 — Navigation (Nav2 Stack)**
- Set up the Nav2 stack with  saved map
- Get autonomous point-to-point navigation working
- Tune the costmaps and planner config for environment

### **Phase 6 — Inventory Logic**
- Define "inventory waypoints" (shelf positions)
- Write a mission planner node that sends the robot through waypoints
- Add basic detection/logging at each waypoint (simulated scan)

### **Phase 7 — Hardware Transition**
- Flash everything to the Pi Zero
- Integrate real LiDAR driver
- Tune for real-world differences

---

## Stack
| Tool | Purpose |
|---|---|
| ROS2 Humble | Stable LTS, great community support |
| Gazebo Classic or Gazebo Harmonic | Simulation |
| SLAM Toolbox | Mapping |
| Nav2 | Autonomous navigation |
| RViz2 | Visualization |
| Python for now (rclpy) | Node development (beginner friendly) |

