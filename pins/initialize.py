from myRPi import GPIO
from mystepper import StepperMotor


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
enable_pin_y = 17
enable_pin_x = 12
step_pin_x = 23
dir_pin_x = 24
mode_pins_x = 14, 15, 18
step_pin_y = 27
dir_pin_y = 22
mode_pins_y = 2, 3, 4
pen_pin = 11
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)
p.start(0)
step_type_x = '1/16'  # micro_steps =  {'Full':1,'Half':2,'1/4':4,'1/8':8,'1/16':16,'1/32':32}
step_type_y = '1/16'  # micro_steps =  {'Full':1,'Half':2,'1/4':4,'1/8':8,'1/16':16,'1/32':32}
full_step_delay = .1

motor_x = StepperMotor(
    enable_pin_x,
    step_pin_x,
    dir_pin_x,
    mode_pins_x,
    step_type_x,
    full_step_delay
)

motor_y = StepperMotor(
    enable_pin_y,
    step_pin_y,
    dir_pin_y,
    mode_pins_y,
    step_type_y,
    full_step_delay
)

motor_x.enable(True)
motor_y.enable(True)
