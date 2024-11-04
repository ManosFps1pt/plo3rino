from pins.initialize import motor_x, motor_y

def disable():
    motor_x.enable(False)
    motor_y.enable(False)
