from motor import *
from units.cm import Cm

class Steps:
    def __init__(self, val: int, motor_type: Motor):
        self.val: int = val
        self.motor_type: Motor = motor_type
        self.cm_per_steps_x = 3.5 / 3880
        self.cm_per_steps_y = 3.5 / 2600


    def to_cm(self) -> Cm:
        if self.motor_type == Motor.x:
            return Cm(self.val * self.cm_per_steps_x)
        elif self.motor_type == Motor.y:
            return Cm(self.val * self.cm_per_steps_y)

if __name__ == '__main__':
    var = Steps(3880, Motor.x)
    print(var)
    print(var.to_cm())
    print(var.val)
    print(var.to_cm().val)
