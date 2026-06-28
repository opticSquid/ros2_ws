import rclpy
from rclpy.node import Node

class CustomNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("hello world!")

def main(args=None):
    rclpy.init(args=args)
    node = CustomNode("example_node_name")
    # keep looping until keyboard interrupt
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
