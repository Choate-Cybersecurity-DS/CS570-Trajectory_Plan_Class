import math

from src.pose2D import Pose2D


class Robot:

    def __init__(self, drive_radius, wheel_radius, revs_per_sec, pose: Pose2D):
        self.drive_radius = drive_radius
        self.wheel_radius = wheel_radius
        self.revs_per_sec = revs_per_sec
        self.left_motor_setting = 0
        self.right_motor_setting = 0
        self.pose = pose

    def set_position(self, pose: Pose2D):
        self.pose = pose

    def set_motors(self, left_motor, right_motor):
        self.left_motor_setting = min(1, max(-1, left_motor))
        self.right_motor_setting = min(1, max(-1, right_motor))

    def left_velocity(self):
        return self.left_motor_setting * self.revs_per_sec * self.wheel_radius * 2 * math.pi

    def right_velocity(self):
        return self.left_motor_setting * self.revs_per_sec * self.wheel_radius * 2 * math.pi

    def run(self, time_step):
        pass


class TankRobot(Robot):

    def __init__(self, drive_radius, wheel_radius, revs_per_sec, pose: Pose2D):
        super(TankRobot, self).__init__(drive_radius, wheel_radius, revs_per_sec, pose)

    def run(self, time_step):
        x = self.pose.x
        y = self.pose.y
        theta = self.pose.theta
        if self.right_velocity() == self.left_velocity():
            x += self.left_velocity() * math.cos(theta) * time_step
            y += self.left_velocity() * math.sin(theta) * time_step
            delta_theta = 0
        else:
            rd = self.right_velocity() * time_step
            ld = self.left_velocity() * time_step
            delta_theta = (ld - rd) / (2 * self.wheel_radius)
            turn_radius = min(rd, ld) / math.fabs(delta_theta)
            dx = (turn_radius + self.wheel_radius) * math.sin(delta_theta)
            dy = (turn_radius + self.wheel_radius) * (1 - math.cos(delta_theta))
            x += math.cos(theta) * dx + math.sin(theta) * dy
            y += -math.sin(theta) * dx + math.cos(theta) * dy
        self.pose = Pose2D(x, y, theta + delta_theta)
