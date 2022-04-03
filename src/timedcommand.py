class TimedCommand:

    def __init__(self, left_motor=0, right_motor=0, start_time=0, end_time=0):
        self.left_motor = left_motor
        self.right_motor = right_motor
        if end_time < start_time:
            raise ValueError("Start time must be before End time")
        else:
            self.start_time = start_time
            self.end_time = end_time

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_left_motor(self):
        return self.left_motor

    def get_right_motor(self):
        return self.right_motor
