import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)
        timer_period = 0.1  # seconds (adjust as needed for "as fast as possible" within reason)
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = AckermannDriveStamped()
        v = self.get_parameter('v').get_parameter_value().double_value
        d = self.get_parameter('d').get_parameter_value().double_value
        msg.drive.speed = v
        msg.drive.steering_angle = d
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: speed=%f, steering_angle=%f' % (v, d))

def main(args=None):
    rclpy.init(args=args)
    node = Talker()

    # Declare parameters
    node.declare_parameter('v', 0.0)
    node.declare_parameter('d', 0.0)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
