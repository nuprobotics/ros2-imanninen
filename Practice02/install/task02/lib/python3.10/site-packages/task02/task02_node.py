# task02/task02_node.py
import rclpy
import sys
from rclpy.node import Node
from std_msgs.msg import String

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        
        # Load parameters
        self.declare_parameter('topic_name', 'no_topic')
        self.declare_parameter('text', 'Hello, ROS2!!!!')

        self.topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        self.get_logger().info(f'Set "topic_name" to {self.topic_name}')

        self.text = self.get_parameter('text').get_parameter_value().string_value
        self.get_logger().info(f'Set "text" to {self.text}')

        self.publisher = self.create_publisher(String, self.topic_name, 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = self.text
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}" to topic "{self.topic_name}"')


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisher()
    
    # Get command-line parameters
    # if len(args) > 1:
    #     node.get_parameter('text').set_parameter_value(String(data=args[1]))
    
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main(sys.argv)
