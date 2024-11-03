from motor import *
from units import *
from pins import *
from typing import Iterable

x_pos: Steps = Steps(0, Motor.x)
y_pos: Steps = Steps(0, Motor.y)


def pendown():
    p.ChangeDutyCycle(2)
    print("pendown")

def penup():
    p.ChangeDutyCycle(4)
    print("penup")


def calibrate() -> None:
    global x_pos, y_pos
    motor_x.run(4200, True)#3880, True) # far right
    motor_y.run(2700, True)#2600, True) # far up
    x_pos = 0
    y_pos = 0
    print("calibrate")


def motor_movement(motor: Motor, move_val: Steps):
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

def goto_steps(point: tuple[Steps, Steps] | list[Steps, Steps]):
    global x_pos, y_pos
    x_target, y_target = point
    dx = x_pos.val - x_target
    dy = y_pos.val - y_target
    motor_movement(Motor.x, dx)
    motor_movement(Motor.y, dy)

def goto_steps_iterable(points: Iterable[Steps, Steps]):
    for i in points:
        goto_steps(i)

def goto_cm(point: tuple[Cm, Cm]):
    point_steps = point
    map(Cm.to_steps, point_steps)
    goto_steps(point_steps)

a = Steps(1000, Motor.x), Steps(100, Motor.x), Steps(6000, Motor.x)

print(goto_cm((Cm(3.5), Cm(3.5))))

