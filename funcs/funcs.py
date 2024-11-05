from motor import *
from units import *
from pins import *
from typing import Iterable

x_pos: Steps = Steps(0, Motor.x)
y_pos: Steps = Steps(0, Motor.y)


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


def motor_movement(motor: Motor, move_val: Steps) -> None:
    global x_pos, y_pos
    if motor == Motor.x:
        if move_val.val > 0:
            motor_x.run(move_val.val, False)
            x_pos.val += move_val.val
        else:
            motor_x.run(abs(move_val.val), True)
            x_pos.val -= move_val.val
    if motor == Motor.y:
        if move_val.val > 0:
            motor_y.run(move_val.val, False)
            y_pos.val += move_val.val
        else:
            motor_y.run(abs(move_val.val), True)
            y_pos.val -= move_val.val

def goto_steps(point: tuple[Steps, Steps] | list[Steps, Steps]) -> None:
    global x_pos, y_pos
    x_target = point[0]
    y_target = point[1]
    dx = x_pos - x_target
    dy = y_pos - y_target
    motor_movement(Motor.x, dx)
    motor_movement(Motor.y, dy)

def goto_steps_iterable(points: Iterable[tuple[Steps, Steps]]) -> None:
    for i in points:
        goto_steps(i)

def goto_cm(point: tuple[Cm, Cm] | list[Cm, Cm]) -> None:
    point_steps: tuple[Steps, Steps] = point[0].to_steps(Motor.x), point[1].to_steps(Motor.y)
    goto_steps(point_steps)

def goto_cm_iterable(points: Iterable[tuple[Cm, Cm]]) -> None:
    for i in points:
        goto_cm(i)

# a = Steps(1000, Motor.x), Steps(100, Motor.x), Steps(6000, Motor.x)

print(goto_cm((Cm(3.5), Cm(3.5))))
