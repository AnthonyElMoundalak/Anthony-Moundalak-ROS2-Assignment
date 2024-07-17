# Anthony-Moundalak-ROS2-Assignment
# Temperature Monitoring System

This ROS 2 package simulates a temperature monitoring system with the following nodes:
- `temperature_publisher`: Publishes random temperature values.
- `threshold_subscriber`: Subscribes to temperature values and triggers alerts if the threshold is exceeded.
- `alert_publisher`: Publishes alert messages.
- `temperature_logger` (Bonus): Logs temperature values to a file.

## Build and Run

```sh
colcon build
source install/setup.bash
ros2 launch temperature_package temp_monitoring_launch.py
```