import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class DiceRoller(Node):
    def __init__(self):
        super().__init__('dice_roller')
        self.publisher_ = self.create_publisher(Int32, 'dice', 10)
        self.timer = self.create_timer(2.0, self.roll_dice)  # every 2 seconds
        self.get_logger().info('Dice Roller Node Started.')

    def roll_dice(self):
        number = random.randint(1, 6)
        msg = Int32()
        msg.data = number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Rolled dice: {number}')

def main(args=None):
    rclpy.init(args=args)
    node = DiceRoller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
