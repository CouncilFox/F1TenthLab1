import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)

    def listener_callback(self, msg):
        new_msg = AckermannDriveStamped()
        new_msg.header.stamp = self.get_clock().now().to_msg()
        new_msg.drive.speed = msg.drive.speed * 3
        new_msg.drive.steering_angle = msg.drive.steering_angle * 3
        self.publisher_.publish(new_msg)
        self.get_logger().info('Relaying: speed=%f, steering_angle=%f' % (new_msg.drive.speed, new_msg.drive.steering_angle))

def main(args=None):
    rclpy.init(args=args)
    node = Relay()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
