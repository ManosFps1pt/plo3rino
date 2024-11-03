from motor import *


class Cm:
    def __init__(self, val: int | float):
        self.val = val
        self.motor_x_steps_cm = 3880 / 3.5
        self.motor_y_steps_cm = 2600 / 3.5

    def to_steps(self, motor: Motor):
        if motor == Motor.x:
            return int(self.val * self.motor_x_steps_cm)
        elif motor == Motor.y:
            return int(self.val * self.motor_y_steps_cm)
        else:
            raise ValueError("Unsupported motor type")
