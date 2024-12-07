from motor import *
from enum import Enum

class Units(Enum):
    Cm: int = 0
    Steps: int = 1


class Unit:
    def __init__(self, motor: Motor, value: int | float, unit: Units):
        self.motor_x_steps = 3880
        self.motor_y_steps = 2600
        self.motor_x_cm = 3.5
        self.motor_y_cm = 3.5

        self.value = value
        self.motor = motor
        self.unit = unit

    def val(self, unit: Units) -> int | float:
        if unit == self.unit:
            return self.value
        elif unit == Units.Cm:
            return (
                    self.value * self.motor_x_cm
                    / self.motor_x_steps
            ) if self.motor == Motor.x else (
                    self.value * self.motor_y_cm
                    / self.motor_y_steps
            )
        elif unit == Units.Steps:
            return int( (
                                self.value * self.motor_x_steps / self.motor_x_cm
                ) if self.motor == Motor.x else (
                    self.value * self.motor_y_steps / self.motor_y_cm
                )
            )
        else:
            raise ValueError("Unsupported unit type")

    def __repr__(self):
        return f"Unit(motor={self.motor.name}, val={self.value}, unit={self.unit.name})"

    def __sub__(self, other):
        val1: float = self.val(Units.Cm)
        if isinstance(other, Unit):
            val2: float = other.val(Units.Cm)
        elif isinstance(other, int):
            val2: float = other
        return Unit(self.motor, val1 - val2, Units.Cm)



if __name__ == '__main__':
    x = Unit(Motor.y, 3.5, Units.Cm)
    print(x.val(Units.Steps))

