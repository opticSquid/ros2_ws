import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
class CustomTurtleOperator(Node):
    def __init__(self, name):
        super().__init__(name)

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # call callback function every 1s
        self.create_timer(1, callback=self.callback)

    def callback(self):
        message = Twist()
        message.linear.x = 1.0
        message.linear.y = 0.0
        message.linear.z = 0.0
        message.angular.x = 0.0
        message.angular.y = 0.0
        message.angular.z = 1.0
        # self.get_logger().info(message)
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    node = CustomTurtleOperator("example_node_name")
    # keep looping until keyboard interrupt
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
