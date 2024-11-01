from stepper import StepperMotor
from time import sleep
import RPi.GPIO as GPIO
import math



class Plotter:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.enable_pin_y = 17
        self.enable_pin_x = 12
        self.step_pin_x = 23
        self.dir_pin_x = 24
        self.mode_pins_x = (14, 15, 18)
        self.step_pin_y = 27
        self.dir_pin_y = 22
        self.mode_pins_y = (2, 3, 4)
        self.pen_pin = 11
        GPIO.setup(11,GPIO.OUT)
        self.p = GPIO.PWM(11, 50)    
        self.p.start(0) 
        self.step_type_x = '1/16'         #microsteps =  {'Full':1,'Half':2,'1/4':4,'1/8':8,'1/16':16,'1/32':32}
        self.step_type_y = '1/16'         #microsteps =  {'Full':1,'Half':2,'1/4':4,'1/8':8,'1/16':16,'1/32':32}
        self.fullstep_delay = .1
        self.motor_x_steps_cm = 3880/3.5
        self.motor_y_steps_cm = 2600/3.5
        self.x_pos = 0
        self.y_pos = 0
        self.accurancy = .5
        self.motor_x = StepperMotor(self.enable_pin_x, self.step_pin_x, self.dir_pin_x, self.mode_pins_x, self.step_type_x, self.fullstep_delay)
        self.motor_y = StepperMotor(self.enable_pin_y, self.step_pin_y, self.dir_pin_y, self.mode_pins_y, self.step_type_y, self.fullstep_delay)
        self.motor_x.enable(True)
        self.motor_y.enable(True)
    
    
    def pendown(self):
        self.p.ChangeDutyCycle(2)
        print("pendown")
        
    def penup(self):
        self.p.ChangeDutyCycle(4)
        print("penup")
    
    def motor_movement(self, motor, move_val):
        if motor == "x":
            if move_val > 0:
                self.motor_x.run(move_val, False)
            else:
                self.motor_x.run(abs(move_val), True)
        if motor == "y":
            if move_val > 0:
                self.motor_y.run(move_val, False)
            else:
                self.motor_y.run(abs(move_val), True)

    def calibrate(self):
        self.motor_x.run(4200, True)#3880, True) # far right
        self.motor_y.run(2700, True)#2600, True) # far up
        self.x_pos = 0
        self.y_pos = 0
        print("calibrate")
    
    
    def cmtosteps(self, motor, val):
        if motor.lower() == "x":
            steps = int(val * self.motor_x_steps_cm)
        elif motor.lower() == "y":
            steps = int(val * self.motor_y_steps_cm)       
        else:
            raise ValueError("not valid motor")
        return steps

    def hypotenuse(self, x, y):
        return math.sqrt(x ** 2 + y ** 2) 

    def lerp(self, pos1, pos2, t):
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        return pos1[0] + dx * t, pos1[1] + dy * t 



        
#    def goto(self, x, y):
#        print("goto start")
#        dx = x - self.x_pos
#        dy = y - self.y_pos
#        size = self.hypotenuse(dx, dy)
#        iterations = size // self.accurancy
#        t = 0
#        tinc = 1 / iterations
#        print(x, y)
#        print(iterations, tinc)
#        for _ in range(int(iterations)):
#            
#            pos = self.lerp((self.x_pos, self.y_pos), (x, y), t)
#            self.motor_movement("x", self.cmtosteps("x", dx / iterations))
#            self.motor_movement("y", self.cmtosteps("y", dy / iterations))
#            t += tinc
#        self.x_pos = pos[0]
#        self.y_pos = pos[1]
#        print(self.x_pos, self.y_pos, "goto done")
#        return

    def goto(self, pos: tuple[int, int]):
        dx = self.x_pos - pos[0]
        dy = self.y_pos - pos[1]
        print(f"goto {dx} {dy}")
        self.motor_movement("x", dx)
        self.motor_movement("y", dy)
        

    def polygon(self, x, y, radx, rady, sides, degreestoadd = 0):
            increment =  360 / sides
            degrees = degreestoadd
            for _ in range(sides + 1):
                degrees += increment
                x_pos = math.cos(math.radians(degrees)) * radx + x
                y_pos = math.sin(math.radians(degrees)) * rady + y
                print("polygon", x_pos, y_pos)
                self.goto((x_pos, y_pos))
                
    def dda(self, x1, y1, x2, y2, format):
        dx = x2 - x1
        dy = y2 - y1
        if format.lower() == "full":
            steps = max(abs(dx), abs(dy))
        elif format.lower() == "goto":
            steps = min(abs(dx), abs(dy))
        else:
            raise ValueError("incorrect format type. You should use 'full' or 'goto'. ")
        try:
            x_inc = dx / steps
            y_inc = dy / steps
        except ZeroDivisionError:
            raise ValueError("cannot create a line that has the length of a pixel. Try making a longer line")
        for _ in range(steps + 1):
            returning_x = round(x1)
            returning_y = round(y1)
            x1 += x_inc
            y1 += y_inc
            yield returning_x, returning_y
            
    def goto_iterable(self, iter):
        for i in iter:
            continue            


    def main(self):
        try:
            self.pendown()
            self.calibrate()
            sleep(1)
            print("motor")
            self.motor_movement("x", 1000)
            self.motor_movement("y", 1000)
            self.goto((3, 3))
        finally:
            print("motors disabled successfully")
            plotter.motor_x.enable(False)
            plotter.motor_y.enable(False)
            self.penup()


plotter = Plotter()
plotter.main()

print("---------| execution done | --------------------")
