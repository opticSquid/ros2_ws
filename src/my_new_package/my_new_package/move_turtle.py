import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from random import uniform
class CustomTurtleOperator(Node):
    def __init__(self, name):
        super().__init__(name)

        self.publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        # call callback function every 1s
        self.create_timer(1, callback=self.callback)

    def callback(self):
        message = Twist()
        message.linear.x = uniform(-1,1)
        message.linear.y = uniform(-1,1)
        message.linear.z = uniform(-1,1)
        message.angular.x = uniform(-1,1)
        message.angular.y = uniform(-1,1)
        message.angular.z = uniform(-1,1)
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
