#!/usr/bin/env python3
########################################################################
# Filename    : RPi-3-servo.py
# Description : Controla un servo motor. 
# Author      : jcondea
# modification: 2020/10/06
########################################################################
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(7)
x1=0
y1=3.1
x2=180
y2=12.3
for i in range(0,20):
    desiredAngle=int(input("Angulo del servo? 0-180="))
    m=(y2-y1)/(x2-x1)
    DC=m*(desiredAngle-x1)+y1
    pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()
