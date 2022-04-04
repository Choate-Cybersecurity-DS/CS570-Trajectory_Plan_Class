import math

from src.pose2D import Pose2D


class Robot:

    def __init__(self, drive_radius: float = 0.15, wheel_radius: float = 0.05,
                 revs_per_sec: float = 60, pose: Pose2D = Pose2D(0, 0, 0)):
        self.drive_radius = drive_radius
        self.wheel_radius = wheel_radius
        self.revs_per_sec = revs_per_sec
        self.left_motor_setting = 0
        self.right_motor_setting = 0
        self.pose = pose

    def max_wheel_speed(self) -> float:
        return self.revs_per_sec * self.wheel_radius * 2 * math.pi

    def max_turn_speed(self) -> float:
        return self.max_wheel_speed() / self.drive_radius

    def set_position(self, pose: Pose2D) -> None:
        self.pose = pose

    def set_motors(self, left_motor, right_motor):
        self.left_motor_setting = min(1, max(-1, left_motor))
        self.right_motor_setting = min(1, max(-1, right_motor))

    def get_left_velocity(self):
        return self.left_motor_setting * self.revs_per_sec * self.wheel_radius * 2 * math.pi

    def get_right_velocity(self):
        return self.right_motor_setting * self.revs_per_sec * self.wheel_radius * 2 * math.pi

    def run(self, time_step):
        pass


class TankRobot(Robot):

    def __init__(self, drive_radius, wheel_radius, revs_per_sec, pose: Pose2D):
        super(TankRobot, self).__init__(drive_radius, wheel_radius, revs_per_sec, pose)

    def run(self, time_step):
        x = self.pose.x
        y = self.pose.y
        theta = self.pose.theta
        if self.get_right_velocity() == self.get_left_velocity():
            x += self.get_left_velocity() * math.cos(theta) * time_step
            y += self.get_left_velocity() * math.sin(theta) * time_step
            delta_theta = 0
        else:
            rd = self.get_right_velocity() * time_step
            ld = self.get_left_velocity() * time_step
            delta_theta = (rd - ld) / (2 * self.drive_radius)
            turn_radius = min(rd, ld) / math.fabs(delta_theta)
            dx = (turn_radius + self.drive_radius) * math.sin(delta_theta)
            dy = (turn_radius + self.drive_radius) * (1 - math.cos(delta_theta))
            x += math.cos(theta) * dx + math.sin(theta) * dy
            y += -math.sin(theta) * dx + math.cos(theta) * dy
        self.pose = Pose2D(x, y, theta + delta_theta)
