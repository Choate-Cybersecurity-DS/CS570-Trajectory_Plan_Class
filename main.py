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

TRACK_RADIUS = .30  # The track radius is 14 cm
WHEEL_RADIUS = .05  # The wheel radius on your tank drive is 8 cm
MAX_ROTATIONS = 10  # The maximum number of rotations your wheels can do is 200 rev per second
START_POSE = Pose2D(4, 2, 0)
END_POSE = Pose2D(5, 1, 1)
SPEED = .1


class MyTrajectoryGenerator(TrajectoryGenerator):

    def generate(self, robot: Robot, end_pose: Pose2D, speed) -> Trajectory:
        # begin turn to get robot to move
        trajectory = Trajectory()
        start_x = robot.pose.x
        start_y = robot.pose.y
        end_x = end_pose.x
        end_y = end_pose.y
        target_direction = math.atan2(end_y - start_y, end_x - start_x)
        delta_theta = target_direction - robot.pose.theta
        first_command = self.point_turn_command(robot, delta_theta, speed, 0)
        trajectory.append(first_command)
        new_start_time = first_command.get_end_time()
        # now move the robot
        distance = math.dist((start_x, start_y), (end_x, end_y))
        second_command = self.move_straight_command(robot, distance, speed, new_start_time)
        new_start_time = second_command.get_end_time()
        trajectory.append(second_command)
        # now the final turn
        delta_theta = end_pose.theta - target_direction
        third_command = self.point_turn_command(robot, delta_theta, speed, new_start_time)
        trajectory.append(third_command)
        return trajectory

    def point_turn_command(self, robot, delta_theta, speed, start_time) -> TimedCommand:
        time_turn_one = math.fabs(delta_theta / (robot.max_turn_speed() * speed))
        speed_one = math.copysign(speed, delta_theta)
        return TimedCommand(-1 * speed_one, speed_one, start_time, start_time + time_turn_one)

    def move_straight_command(self, robot, distance, speed, start_time) -> TimedCommand:
        time = distance / (speed * robot.max_wheel_speed())
        return TimedCommand(speed, speed, start_time, start_time + time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_robot = TankRobot(TRACK_RADIUS, WHEEL_RADIUS, MAX_ROTATIONS, START_POSE)
    print("Linear max speed: " + str(my_robot.max_wheel_speed()))
    print("Max Angular sped: " + str(my_robot.max_turn_speed()))
    trajectory_generator = MyTrajectoryGenerator()

    trajectory = trajectory_generator.generate(my_robot, END_POSE, SPEED)
    # trajectory=Trajectory()
    # trajectory.append(TimedCommand(-.1, .1, 0, .0416))
    robot_runner = RobotRunner(my_robot, trajectory)
    robot_runner.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
