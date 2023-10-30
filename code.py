import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

left_motor_backwards = board.GP12
left_motor_foward = board.GP13
right_motor_foward = board.GP14
right_motor_backwards = board.GP15

pwm_La = pwmio.PWMOut(left_motor_backwards, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_foward, frequency=10000)
pwm_Ra = pwmio.PWMOut(right_motor_foward, frequency=10000)
pwm_Rb = pwmio.PWMOut(right_motor_backwards, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0
Right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
Right_Motor_speed = 0

def forward():
    Left_Motor_speed = -1 #moves left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1#forward
    Right_Motor.throttle = Right_Motor_speed
def backwards() :
    Right_Motor_speed = -1#backward
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 1#backwards
    Left_Motor.throttle = Left_Motor_speed
def left() :
    Right_Motor_speed = 0#backward
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 1 #moves left motor backwards
    Left_Motor.throttle = Left_Motor_speed
def right() :
    Left_Motor_speed = 0 #moves left motor backwards
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1#backward
    Right_Motor.throttle = Right_Motor_speed




while True:
    left()
    time.sleep(4)
    backwards()
    time.sleep(1)
    forward()
    time.sleep(6)
    right()
    time.sleep(3)
    forward()
    time.sleep (1)
    left()
    time.sleep (7)
'''
    Left_Motor_speed = -1 #moves left motor foward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1#foward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(5)
    Right_Motor_speed = -1#backward
    Right_Motor.throttle = Right_Motor_speed
    Left_Motor_speed = 1#backwards
    time.sleep(5)
    Right_Motor_speed = 0#backward
    Left_Motor_speed = 1 #moves left motor backwards
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(5)
    Left_Motor_speed = 0 #moves left motor backwards
    Right_Motor_speed = 1#backward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(5)

    time.sleep(5)
'''
