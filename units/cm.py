from motor import *
from units import Steps


class Cm:
    def __init__(self, val: int | float):
        self.val = val
        self.motor_x_steps_cm = 3880 / 3.5
        self.motor_y_steps_cm = 2600 / 3.5

    def to_steps(self, motor: Motor) -> Steps:
        if motor == Motor.x:
            return Steps(int(self.val * self.motor_x_steps_cm), motor.x)
        elif motor == Motor.y:
            return Steps(int(self.val * self.motor_y_steps_cm), motor.y)
        else:
            raise ValueError("Unsupported motor type")
