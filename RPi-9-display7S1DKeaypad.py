#!/usr/bin/env python3
########################################################################
# Filename    : RPi-9-display7S1DKeypad.py
# Description : Controla un Display de 7 Segmentos y 1 digito con un Keypad. 
# Author      : jcondea
# modification: 2020/10/06
########################################################################
import RPi.GPIO as GPIO
import Keypad       #import module Keypad
from time import sleep

ROWS=4
COLS=4
keys = [ '1','2','3','A',
         '4','5','6','B',
         '7','8','9','C',
         '*','0','#','D']
rowsPins=[29,31,33,35]
colsPins=[19,15,13,11]
def print0():
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,True)
    GPIO.output(e,True)
    GPIO.output(f,True)
    GPIO.output(g,False)
    GPIO.output(DP,True)
def print1():
    GPIO.output(a,False)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,False)
    GPIO.output(e,False)
    GPIO.output(f,False)
    GPIO.output(g,False)
    GPIO.output(DP,True)
def print2():
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,False)
    GPIO.output(d,True)
    GPIO.output(e,True)
    GPIO.output(f,False)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def print3():
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,True)
    GPIO.output(e,False)
    GPIO.output(f,False)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def print4():
    GPIO.output(a,False)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,False)
    GPIO.output(e,False)
    GPIO.output(f,True)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def print5():
    GPIO.output(a,True)
    GPIO.output(b,False)
    GPIO.output(c,True)
    GPIO.output(d,True)
    GPIO.output(e,False)
    GPIO.output(f,True)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def print6():
    GPIO.output(a,True)
    GPIO.output(b,False)
    GPIO.output(c,True)
    GPIO.output(d,True)
    GPIO.output(e,True)
    GPIO.output(f,True)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def print7():
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,False)
    GPIO.output(e,False)
    GPIO.output(f,False)
    GPIO.output(g,False)
    GPIO.output(DP,True)
def print8():
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,True)
    GPIO.output(e,True)
    GPIO.output(f,True)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def print9():
    GPIO.output(a,True)
    GPIO.output(b,True)
    GPIO.output(c,True)
    GPIO.output(d,True)
    GPIO.output(e,False)
    GPIO.output(f,True)
    GPIO.output(g,True)
    GPIO.output(DP,True)
def printClear():
    GPIO.output(a,False)
    GPIO.output(b,False)
    GPIO.output(c,False)
    GPIO.output(d,False)
    GPIO.output(e,False)
    GPIO.output(f,False)
    GPIO.output(g,False)
    GPIO.output(DP,False)


GPIO.setmode(GPIO.BOARD)
a=12
b=16
c=18
d=22
e=32
f=36
g=38
DP=40
GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(d,GPIO.OUT)
GPIO.setup(e,GPIO.OUT)
GPIO.setup(f,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(DP,GPIO.OUT)

keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #create Keypad object
keypad.setDebounceTime(50)      #set the debounce time

printClear()

while(1):
    key = keypad.getKey()       #obtain the state of keys
    if(key != keypad.NULL):     #if there is key pressed, print its key code.
        if key=='0':
            print0()
            #sleep(.5)
        elif key=='1':
            print1()
            #sleep(.5)
        elif key=='2':
            print2()
            #sleep(.5)
        elif key=='3':
            print3()
            #sleep(.5)
        elif key=='4':
            print4()
            #sleep(.5)
        elif key=='5':
            print5()
            #sleep(.5)
        elif key=='6':
            print6()
            #sleep(.5)
        elif key=='7':
            print7()
            #sleep(.5)
        elif key=='8':
            print8()
            #sleep(.5)
        elif key=='9':
            print9()
            #sleep(.5)

GPIO.clenaup()

