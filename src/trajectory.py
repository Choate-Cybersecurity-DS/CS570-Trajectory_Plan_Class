from src.timedcommand import TimedCommand


class Trajectory(list):

    def append(self, my_command: TimedCommand) -> None:
        print(type(my_command))
        if type(my_command) == TimedCommand:
            super().append(my_command)
        else:
            raise TypeError("Must be TimedCommand")


if __name__ == "__main__":
    x = Trajectory()
    print(type(x))
    y = TimedCommand(.3, .4, 40, 10)
    x.append(y)
