# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:28:10 2018

@author: kevinwa
"""
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

PWM1 = 12
GPIO.setwarings(False)

GPIO.setup(PWM1, GPIO.OUT, inital=GPIO.LOW)

Servo1 = GPIO.PWM(PWM1, 50)
Servo1.start(0)

def SetServoAngle(angle):
    print("Current Angle: ", angle)
    duty = 2.5 + 10 * angle / 180
    Servo1.ChangeDutyCycle(2.5 + 10 * angle / 180)

for i in range(1, 5): 
    SetServoAngle(30)
    time.sleep(0.1)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(90)
    time.sleep(0.1)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(150)
    time.sleep(0.1)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)
    SetServoAngle(90)
    time.sleep(0.1)
    Servo1.ChangeDutyCycle(0)
    time.sleep(0.4)