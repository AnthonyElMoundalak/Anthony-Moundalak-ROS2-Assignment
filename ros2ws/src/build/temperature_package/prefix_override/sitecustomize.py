import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/anthonyubuntu/Desktop/inmind/session5/Anthony-Moundalak-ROS2-Assignment/ros2ws/src/install/temperature_package'
