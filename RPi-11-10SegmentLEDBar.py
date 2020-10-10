#!/usr/bin/env python3
########################################################################
# Filename    : RPi-11-10SegmentLEDBar.py
# Description : Prende en secuencia y luego apaga en secuencia los 10 segmentos de la barra. 
# Author      : jcondea
# modification: 2020/10/10
########################################################################
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
led1=7
led2=11
led3=12
led4=13
led5=15
led6=16
led7=18
led8=22
led9=29
led10=31
leds=[led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
GPIO.setup(leds, GPIO.OUT, initial=0)
time.sleep(1)

while True:
    for led in leds:
       GPIO.output(led, 1) # ON
       time.sleep(0.1)
    for led in reversed(leds):
       time.sleep(0.1)
       GPIO.output(led, 0) # OFF
GPIO.cleanup()
