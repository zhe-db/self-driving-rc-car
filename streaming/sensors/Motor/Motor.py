import time
import RPi.GPIO as GPIO
import datetime
import json

class Motor:
    def __init__(self):
        self.ENA = 13
        self.ENB = 20
        self.IN1 = 19
        self.IN2 = 16
        self.IN3 = 21
        self.IN4 = 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.ENA,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.IN1,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.IN2,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.ENB,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.IN3,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(self.IN4,GPIO.OUT,initial=GPIO.LOW)
        self.ENA_PWM = GPIO.PWM(self.ENA, 100)
        self.ENB_PWM = GPIO.PWM(self.ENB, 100)


    def Motor_Forward(self):
        self.PWM_Clean()
        print('motor_forward')
        GPIO.output(self.ENA,True)
        GPIO.output(self.ENB,True)
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,True)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,True)

    def Motor_Backward(self):
        self.PWM_Clean()
        print('motor backward')
        GPIO.output(self.ENA, True)
        GPIO.output(self.ENB, True)
        GPIO.output(self.IN1, True) 
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, True)
        GPIO.output(self.IN4, False)
    
    def Motor_ForwardLeft(self):
        self.PWM_Clean()
        print('motor_forwardleft')
        GPIO.output(self.ENA,True)
        GPIO.output(self.ENB,False)
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,True)
        GPIO.output(self.IN3,True)
        GPIO.output(self.IN4,True)
        time.sleep(0.1)
        self.Motor_Stop()
    
    def Motor_ForwardRight(self):
        self.PWM_Clean()
        print('motor_forwardright')
        GPIO.output(self.ENA,False)
        GPIO.output(self.ENB,True)
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,True)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,True)
        time.sleep(0.1)
        self.Motor_Stop()


    def Motor_TurnRight(self):
        self.PWM_Clean()
        print('motor_turnright')
        GPIO.output(self.ENA,True)
        GPIO.output(self.ENB,True)
        GPIO.output(self.IN1,True)
        GPIO.output(self.IN2,False)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,True)
        time.sleep(0.1)
        self.Motor_Stop()
 
    def Motor_TurnLeft(self):
        self.PWM_Clean()
        print('motor_turnleft')
        # self.ENB_PWM.ChangeDutyCycle(100)
        GPIO.output(self.ENA,True)
        GPIO.output(self.ENB,True)
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,True)
        GPIO.output(self.IN3,True)
        GPIO.output(self.IN4,False)
        time.sleep(0.1)
        self.Motor_Stop()

    def Motor_Reverse(self):
        self.PWM_Clean()
        print('motor_reverse')
        GPIO.output(self.ENA,True)
        GPIO.output(self.ENB,True)
        GPIO.output(self.IN1,True)
        GPIO.output(self.IN2,False)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,True)
        time.sleep(0.3)
        self.Motor_Stop() 

    
    def Motor_Stop(self):
        self.PWM_Clean()
        print('motor_stop')
        GPIO.output(self.ENA,False)
        GPIO.output(self.ENB,False)
        GPIO.output(self.IN1,False)
        GPIO.output(self.IN2,False)
        GPIO.output(self.IN3,False)
        GPIO.output(self.IN4,False)

    def PWM_Clean(self):
        self.ENA_PWM.ChangeDutyCycle(100)
        self.ENB_PWM.ChangeDutyCycle(100)
