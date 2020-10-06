#!/usr/bin/env python3
########################################################################
# Filename    : Keypad.py
# Description : Prende y apaga un LED por [n] veces. 
# Author      : jcondea
# modification: 2020/10/06
########################################################################
import time
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#red=11
GPIO.setmode(GPIO.BCM)
red=17
GPIO.setup(red, GPIO.OUT)
blink_num = int(input("Cuantas veces?"))
for i in range(0,blink_num):
    GPIO.output(red,True)
    time.sleep(1)
    GPIO.output(red,False)
    time.sleep(1)
GPIO.cleanup()

