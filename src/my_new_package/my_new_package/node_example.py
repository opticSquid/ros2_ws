import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node("example_node_name")
    node.get_logger().info("hello world!")
    # keep looping until keyboard interrupt
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
