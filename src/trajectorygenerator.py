from src.pose2D import Pose2D
from src.trajectory import Trajectory


class TrajectoryGenerator:

    def generate(self, start_pose: Pose2D, end_Pose: Pose2D) -> Trajectory:
        # The trajectories should be 3-tuples (.5, .5, 300)
        # this would indicate that we would run the robot at half
        # speed for both motors, starting at 300 milliseconds.

        pass
