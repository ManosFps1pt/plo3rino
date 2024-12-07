from sympy.physics.units.systems.si import units

from motor import *
from units import *
from pins import *
from typing import Iterable

x_pos: Unit = Unit(Motor.x, 0, Units.Steps)
y_pos: Unit = Unit(Motor.y, 0, Units.Steps)


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
    x_pos = 0
    y_pos = 0
    print("calibrate")


def motor_movement(motor: Motor, move_val: Unit) -> None:
    global x_pos, y_pos
    print(x_pos, move_val)
    if motor == Motor.x:
        if move_val.val(Units.Steps) > 0:
            motor_x.run(move_val.val, False)
            x_pos.val += move_val.val
        else:
            motor_x.run(abs(move_val.val(Units.Steps)), True)
            x_pos.val -= move_val.val
    if motor == Motor.y:
        if move_val.val(Units.Steps) > 0:
            motor_y.run(move_val.val, False)
            y_pos.val += move_val.val
        else:
            motor_y.run(abs(move_val.val(Units.Steps)), True)
            y_pos.val -= move_val.val

def goto(point: tuple[Unit, Unit] | list[Unit, Unit]) -> None:
    global x_pos, y_pos
    x_target = point[0]
    y_target = point[1]
    print(f"{x_target=}")
    dx = x_pos - x_target
    dy = y_pos - y_target
    motor_movement(Motor.x, dx)
    motor_movement(Motor.y, dy)
    print(f"goto {x_target=}, {y_target=}")


def goto_iterable(points: Iterable[tuple[Unit, Unit]]) -> None:
    for i in points:
        goto(i)




# a = Steps(1000, Motor.x), Steps(100, Motor.x), Steps(6000, Motor.x)
