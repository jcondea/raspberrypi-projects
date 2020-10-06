#!/usr/bin/env python3
########################################################################
# Filename    : RPi-2-bright.py
# Description : Cambia el brillo de un LED. 
# Author      : jcondea
# modification: 2020/10/06
########################################################################
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
red=11
GPIO.setup(red, GPIO.OUT)
my_pwm=GPIO.PWM(red,100)
my_pwm.start(0)
while(1):
    bright=input("How bright do you want LED?(1-6) ")
    my_pwm.ChangeDutyCycle(2**bright)
my_pwm.stop()
GPIO.cleanup()
