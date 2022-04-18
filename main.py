# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math

from src.pose2D import Pose2D
from src.robot import TankRobot, Robot
from src.robotrunner import RobotRunner
from src.timedcommand import TimedCommand
from src.trajectory import Trajectory
from src.trajectorygenerator import TrajectoryGenerator

TRACK_RADIUS = .15  # The track radius is 14 cm
WHEEL_RADIUS = .08  # The wheel radius on your tank drive is 8 cm
MAX_ROTATIONS = 10  # The maximum number of rotations your wheels can do is 200 rev per second
START_POSE = Pose2D(4, 2, 0)
END_POSE = Pose2D(5, 1, 1)
SPEED = .2


class MyTrajectoryGenerator(TrajectoryGenerator):

    def generate(self, robot: Robot, end_pose: Pose2D, speed) -> Trajectory:
        # begin turn to get robot to move


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_robot = TankRobot(TRACK_RADIUS, WHEEL_RADIUS, MAX_ROTATIONS, START_POSE)
    trajectory_generator = MyTrajectoryGenerator()
    trajectory = trajectory_generator.generate(my_robot, END_POSE, SPEED)
    robot_runner = RobotRunner(my_robot, trajectory)
    robot_runner.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
