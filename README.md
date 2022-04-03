# CS570 Tank Drive Trajectory Plan

In this task, you will be given two poses, and need to find a series of settings for the robot that will move the robot
from one trajectory to another. Use the following constants in making your plan.

```
TRACK_RADIUS = 14 # The track radius is 14 cm
WHEEL_RADIUS = 8 # The wheel radius on your tank drive is 8 cm
MAX_ROTATIONS = 200 # The maximum number of rotations your wheels can do is 200 rev per second
 ```

There is a ```Pose2D``` class that we use to record different poses. The code for Pose2D is:

```commandline
class Pose2D:

    def __init__(self, x, y, theta):
        self.x=x
        self.y=y
        self.theta=theta
```

Your task is to create a ```TrajetoryGenerator``` class. This class will have a method called ```generate``` that will
take a start pose and an end pose, and create a list ```RobotSettings``` that will guide a robot from the starting pose
to the end pose. 

