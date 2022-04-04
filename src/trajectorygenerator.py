from src.pose2D import Pose2D
from src.robot import Robot
from src.trajectory import Trajectory


class TrajectoryGenerator:

    def generate(self, robot: Robot, start_pose: Pose2D, end_Pose: Pose2D) -> Trajectory:
        # The trajectory should be a list should be 4-tuples (.5, .5, 0.0, 300)
        # these 4-tuples are called TimedCommands
        # this would indicate that we would run the robot at half
        # speed for both motors, starting at 0.0 milliseconds and continuing for 300 seconds.

        pass
