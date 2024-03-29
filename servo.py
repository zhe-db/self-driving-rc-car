import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PWM1=25
GPIO.setwarnings(False)

GPIO.setup(PWM1, GPIO.OUT, initial=GPIO.LOW)
Servo1 = GPIO.PWM(PWM1, 50)
Servo1.start(0)

def SetServoAngle(angle):
    print("Current Angle: ", angle)
    duty = 2.5 + 10 * angle / 180
    Servo1.ChangeDutyCycle(2.5 + 10 * angle / 180)


for i in range(1, 1): 
    SetServoAngle(120)
    time.sleep(0.4)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(90)
    time.sleep(0.4)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(0)
    time.sleep(0.4)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(0)
    time.sleep(0.4)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(0)