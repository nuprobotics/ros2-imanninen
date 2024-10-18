import rclpy
from rclpy.node import Node
from std_msgs.msg import String 

class MyFirstNode(Node):
    def __init__(self):
        super(MyFirstNode, self). __init__ ('my_first_node')
        self.subscriber = self.create_subscription(String, '/spgc/sender', self.subscriber_callback, qos_profile=10)

    def subscriber_callback(self, msg):
        self.get_logger().info(f"{msg.data}")



def main():
    rclpy.init()
    node = MyFirstNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
