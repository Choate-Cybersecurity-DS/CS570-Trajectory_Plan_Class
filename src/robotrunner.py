from src.robot import Robot
from src.timedcommand import TimedCommand
from src.trajectory import Trajectory


class RobotRunner:

    def __init__(self, robot: Robot, trajectory: Trajectory):
        self.robot = robot
        self.trajectory = trajectory
        self.time_step = .020
        self.time = 0

    def get_next_trajectory(self) -> TimedCommand:
        next_trajectory = self.trajectory.pop(0)
        return TimedCommand(next_trajectory.get_left_motor(), next_trajectory.get_right_motor(), \
                            next_trajectory.get_start_time(), next_trajectory.get_end_time())

    def increase_time(self):
        self.time += self.time_step

    def print_robot_status(self):
        print(
            f"The robot is at ({self.robot.pose.x}, {self.robot.pose.y}) heading {self.robot.pose.theta} at {self.time}")

    def run(self):

        while len(self.trajectory) > 0:
            next_trajectory = self.get_next_trajectory()
            left_motor = next_trajectory.get_left_motor()
            right_motor = next_trajectory.get_right_motor()
            start_time = next_trajectory.get_start_time()
            end_time = next_trajectory.get_end_time()
            while self.time < end_time:
                self.robot.set_motors(left_motor, right_motor)
                self.robot.run(.02)
                self.print_robot_status()
                self.increase_time()
