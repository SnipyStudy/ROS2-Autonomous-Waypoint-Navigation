import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
import time


class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self.navigator = BasicNavigator()
        self.navigator.waitUntilNav2Active()

        # Define waypoints
        waypoints = []
        for x, y in [(1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]:
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.pose.position.x = x
            pose.pose.position.y = y
            pose.pose.orientation.w = 1.0
            waypoints.append(pose)

        self.navigator.followWaypoints(waypoints)
        while not self.navigator.isTaskComplete():
            time.sleep(0.5)

        self.get_logger().info('Done navigating!')


def main():
    rclpy.init()
    WaypointNavigator()
    rclpy.shutdown()
