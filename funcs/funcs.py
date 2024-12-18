from axis import *
from units import *
from pins import *
from typing import Iterable


x_pos: Length = Length(Axis.x, 0, Units.Steps)
y_pos: Length = Length(Axis.y, 0, Units.Steps)


def pendown() -> None:
    p.ChangeDutyCycle(2)
    print("pendown")

def penup() -> None:
    p.ChangeDutyCycle(4)
    print("penup")


def calibrate() -> None:
    global x_pos, y_pos
    motor_x.run(4200, True)
    motor_y.run(2700, True)
    x_pos.set_steps(0)
    y_pos.set_steps(0)
    print("calibrate")


def motor_movement(motor: Axis, move_val: Length) -> None:
    global x_pos, y_pos
    print(x_pos, move_val)
    if motor == Axis.x:
        if move_val.get_steps() > 0:
            motor_x.run(move_val.get_steps(), False)
            x_pos += move_val
        else:
            motor_x.run(abs(move_val.get_steps()), True)
            x_pos -= move_val
    if motor == Axis.y:
        if move_val.get_steps() > 0:
            motor_y.run(move_val.get_steps(), False)
            y_pos += move_val
        else:
            motor_y.run(abs(move_val.get_steps()), True)
            y_pos -= move_val

def goto(point: tuple[Length, Length] | list[int, int]) -> None:
    global x_pos, y_pos
    x_target = point[0]
    y_target = point[1]
    x_pos.to_steps()
    y_pos.to_steps()
    dx = x_pos - x_target
    dy = y_pos - y_target
    motor_movement(Axis.x, dx)
    motor_movement(Axis.y, dy)
    print(f"goto {x_target=}, {y_target=}")


def goto_iterable(points: Iterable[tuple[Length, Length]]) -> None:
    for i in points:
        goto(i)




# a = Steps(1000, Motor.x), Steps(100, Motor.x), Steps(6000, Motor.x)
