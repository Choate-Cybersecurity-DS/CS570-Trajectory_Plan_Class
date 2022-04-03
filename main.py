# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from src.pose2D import Pose2D
from src.robot import TankRobot
from src.robotrunner import RobotRunner
from src.timedcommand import TimedCommand
from src.trajectory import Trajectory
from src.trajectorygenerator import TrajectoryGenerator


class MyTrajectoryGenerator(TrajectoryGenerator):

    def generate(self, start_pose: Pose2D, end_pose: Pose2D) -> Trajectory:
        first_command = TimedCommand(.3, .3, 0, 10)
        trajectory = Trajectory()
        trajectory.append(first_command)
        return trajectory


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_robot = TankRobot(.30, .04, 500, Pose2D(10, 10, 1))
    trajectory_generator = MyTrajectoryGenerator()
    trajectory = trajectory_generator.generate(None, None)
    robot_runner = RobotRunner(my_robot, trajectory)
    robot_runner.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
