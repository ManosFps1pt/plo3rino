from axis import *
from enum import Enum


class Units(Enum):
    Cm: int = 0
    Steps: int = 1


class Length:
    def __init__(self, motor: Axis, value: int | float, unit: Units):
        self.__motor_x_steps: int = 3880
        self.__motor_y_steps: int = 2600
        self.__motor_x_cm: float = 3.5
        self.__motor_y_cm: float = 3.5

        self.__value: int | float = value
        self.__motor: Axis = motor
        self.__unit: Units = unit


    def  to_cm(self) -> None:
        if self.__unit == Units.Cm:
            return None
        self.__unit = Units.Cm
        self.__value= (
            self.__value * (
                self.__motor_x_cm /
                self.__motor_x_steps
            )
        ) if self.__motor == Axis.x else (
            self.__motor_y_cm /self.__motor_y_steps
        )

    def to_steps(self) -> None:
        if self.__unit == Units.Cm:
            return None
        self.__unit = Units.Steps
        self.__value =  int( (
                self.__value * (
                    self.__motor_x_steps /
                    self.__motor_x_cm
                )
            ) if self.__motor == Axis.x else (
                self.__motor_y_steps /
                self.__motor_y_cm
            )
        )

    def get_cm(self) -> int | float:
        self.to_cm()
        return self.__value

    def get_steps(self) -> int:
        self.to_steps()
        return self.__value

    def set_cm(self, val: float | int) -> None:
        self.__unit = Units.Cm
        self.__value = val

    def set_steps(self, val: int) -> None:
        self.__unit = Units.Steps
        self.__value = val

    def change_cm(self, val: float | int) -> None:
        self.to_cm()
        self.__value += val

    def change_steps(self, val: int) -> None:
        self.to_steps()
        self.__value += val

    def __add__(self, other):
        if isinstance(other, Length):
            if self.__motor != other.__motor:
                raise ValueError(f"Motor axes do not match: {self.__motor.name} and {other.__motor.name}")
            self.to_cm()
            other.to_cm()
            return Length(self.__motor, self.__value + other.__value, Units.Cm)
        elif isinstance(other, int):
            return Length(self.__motor, self.__value + other, self.__unit)
        else:
            raise ValueError(f"Unsupported operand type(s) for +: '{Length.__name__}' and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Length):
            if self.__motor!= other.__motor:
                raise ValueError(f"Motor axes do not match: {self.__motor.name} and {other.__motor.name}")
            self.to_cm()
            other.to_cm()
            return Length(self.__motor, self.__value - other.__value, Units.Cm)
        elif isinstance(other, int):
            return Length(self.__motor, self.__value - other, self.__unit)
        else:
            raise ValueError(f"Unsupported operand type(s) for -: '{Length.__name__}' and {type(other)}")

    def __repr__(self):
        return f"Length(motor={self.__motor.name}, val={self.__value}, unit={self.__unit.name})"


if __name__ == '__main__':
    x = Length(Axis.y, 3.5, Units.Cm)
    print(x.get_steps())

