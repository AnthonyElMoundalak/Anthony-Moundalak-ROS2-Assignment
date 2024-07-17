import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscription = self.create_subscription(
            Float32, 'temperature', self.listener_callback, 10)
        self.log_file = open('log_file.txt', 'a')

    def listener_callback(self, msg):
        log_entry = f'{self.get_clock().now().to_msg().sec} : {msg.data}\n'
        self.log_file.write(log_entry)
        self.get_logger().info(f'Logged temperature: {msg.data}')

    def destroy_node(self):
        self.log_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureLogger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
