from motor import *

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

    def __sub__(self, other):
        return Cm(self.val - other.val)



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



if __name__ == '__main__':
    var1 = Steps(3880, Motor.x)
    var2 = Steps(2600, Motor.y)
    print(var1)
    print(var1.to_cm())
    print(var1.val)
    print(var1.to_cm().val)
    print(var2 - var1)
