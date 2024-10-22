import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class MyService(Node):
    def __init__(self):
        super(MyService, self).__init__("my_service")
        self.declare_parameter('service_name', '/trigger_service')
        self.declare_parameter('default_string', 'No service available')

        self.service_name = self.get_parameter('service_name').get_parameter_value().string_value
        self.default_string = self.get_parameter('default_string').get_parameter_value().string_value

        self.stored_string = ("default value"
                              "")
        self.client = self.create_client(Trigger, "/spgc/trigger")

        if not self.client.wait_for_service(1.0):
            self.get_logger().info(f"Service {self.service_name} not available. Using default value.")
            self.stored_string = self.default_string
            self.get_logger().info(f"Updated stored string.")
        else:
            future = self.client.call_async(Trigger.Request())
            self.get_logger().info(" Waiting for service ... ")
            rclpy.spin_until_future_complete(self, future)
            self.stored_string = future.result().message
            self.get_logger().info(f"Updated stored string: {self.stored_string}")

        self.service = self.create_service(Trigger, self.service_name, self.service_cb)

    def service_cb(self, request, response):
        response.success = True
        response.message = self.stored_string
        return response

def main(args=None):
    rclpy.init(args=args)
    my_service = MyService()
    rclpy.spin(my_service)
    my_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()