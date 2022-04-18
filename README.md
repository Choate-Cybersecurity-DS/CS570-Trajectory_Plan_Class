# CS570 Tank Drive Trajectory Plan

In this task, you will be given two poses, and need to find a series of settings for the robot that will move the robot
from one trajectory to another. Use the following constants in making your plan.

```
TRACK_RADIUS = .15 # The track radius is 15 cm
WHEEL_RADIUS = .05 # The wheel radius on your tank drive is 5 cm
MAX_ROTATIONS = 10 # The maximum number of rotations your wheels can do is 200 rev per second

 ```

Your task is to create a ```TrajectoryGenerator``` class. This class will have a method called ```generate``` that will
take a start pose and an end pose, and create a list ```RobotSettings``` that will guide a robot from the starting pose
to the end pose.

## API

Here are the classes that have been defined in this project. You only have to write one method of one
class, ```Trajectory Generator``` (though it may be helpful to write some helper methods).

### class Pose

The ```Pose``` class is a data class this is simply to keep track of the x, y, and theta.

```
class: Pose2D:

    def __init__(self, x, y, theta):
 
    def get_x(self):
    
    def get_y(self):
    
    def get_theta(self):
```

### class: TankRobot

The ```Robot``` class is a general class that contains information and methods about the robot.

```
class TankRobot:

    def __init__(self, drive_radius:float=0.15, wheel_radius:float=0.05, 
                 revs_per_sec:float=60, pose: Pose2D=Pose2D(0,0,0)):
```

To create a ```Robot``` you need to put in a drive radius, a wheel radius, revolutions per second and a ```Pose```.

```
    def get_max_linear_speed()
``` 

give the maximum forward velocity you can get with the robot.

```
    def get_max_angular_speed(self) -> float:      
```

This method gives the maximum angular velocity.

```
    def set_position(self, pose: Pose2D)->None:
```

Allows you to set a new ```Pose``` for the ```Robot```.

```
    def set_motors(self, left_motor, right_motor): 
```

Allows you to set motor speeds between 1 and -1 for the left and right motors

```
    def get_left_velocity(self):
```

Get the left velocity

```
    def get_right_velocity(self):
 ```

Get the right velocity

 ```
    def run(self, time_step):
        pass
```

run the robot forward for a given time step.

### class: TimedCommand

This class is a data clas the records the settings for the robot motors and when the ```Robot``` should execute those
orders.

```
class TimedCommand:

    def __init__(self, left_motor=0, right_motor=0, start_time=0, end_time=0):
```

When you make a ```TimedCommnand``` you need settings for left motor and right motor and a start time and end time.

```
    def get_start_time(self):
```

``` 
    def get_end_time(self):
```

```
    def get_left_motor(self):
``` 

```
    def get_right_motor(self):
```

```
    def __str__(self):
```

You can also print a ```TimedCommand``` to get a nice text version of its values.

### class: Trajectory

```
class Trajectory(list):
```

A ```Trajectory``` is a list of ```TimedCommand``` objects. Use the append method to add a
```TimedCommand``` to a ```Trajectory```.

```
    def append(self, my_command: TimedCommand) -> None:
```

### class: RobotRunner

```RobotRunner``` is a class that runs a robot through a ```Trajectory``` and reports out the various poses that it goes
through. It keeps track of time, and starts at time equals 0 and increases the time by 0.02 seconds.

```
class RobotRunner:

    def __init__(self, robot: Robot, trajectory: Trajectory):
```

When initialized RobotRunner needs a ```Robot``` and a ```Trajectory```.

```
    def get_next_command(self) -> TimedCommand:
```  

Pulls the next ```TimedCommand``` from  ```Trajectory``` starting with the first in the list.

```
    def increase_time(self):
```

Increase the time by 0.02 seconds.

```
    def print_robot_status(self):
```

Print out where the ```Robot``` is at this time.

```
    def run(self):
```

Run the ```Robot``` through the ```Trajectory``` updating after each time step (0.02 seconds)

### class: TrajectoryGenerator

A ```TrajectoryGenerator``` has no initializer. It's only method is generate. This method takes 2 ```Pose``` objects and
returns a ```Trajectory``` that moves from one to the other.

```
class TrajectoryGenerator:

    def generate(self, robot: Robot, start_pose: Pose2D, end_Pose: Pose2D) -> Trajectory:
```