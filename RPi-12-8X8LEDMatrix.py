#!/usr/bin/env python3
########################################################################
# Filename    : RPi-12-8X8LEDMatrix.py
# Description : Imprime caracteres en una matriz led de 8X8. 
# Author      : jcondea
# modification: 2020/10/22
########################################################################
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
pin1=7 
pin2=11
pin3=12
pin4=13
pin5=15
pin6=16
pin7=18
pin8=22
pin9=29
pin10=31
pin11=32
pin12=33
pin13=35
pin14=36
pin15=37
pin16=38
positives=[pin9, pin14, pin8, pin12, pin1, pin7, pin2, pin5]
negatives=[pin13, pin3, pin4, pin10, pin6, pin11, pin15, pin16]
GPIO.setup(positives, GPIO.OUT, initial=0)
GPIO.setup(negatives, GPIO.OUT, initial=0)

def printCharacter(character):
   posRow=0    
   for i in character:
      for z in range(0,8):
          GPIO.output(positives[z], False)       
      GPIO.output(positives[posRow], True)       
      posColumn=0
      for j in i:
         GPIO.output(negatives[posColumn], j)
         posColumn+=1
      posRow+=1   
      time.sleep(.001)

A=[[1,0,0,0,1,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,0,0,0,0,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,1,1,1,0,1,1,1],
  [1,1,1,1,1,1,1,1]]


B=[[0,0,0,0,1,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,0,0,0,1,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,0,0,0,1,1,1,1],
  [1,1,1,1,1,1,1,1]]

C=[[1,0,0,0,1,1,1,1],
  [0,1,1,1,0,1,1,1],
  [0,1,1,1,1,1,1,1],
  [0,1,1,1,1,1,1,1],
  [0,1,1,1,1,1,1,1],
  [0,1,1,1,0,1,1,1],
  [1,0,0,0,1,1,1,1],
  [1,1,1,1,1,1,1,1]]

D=[[0,0,0,0,1,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,0,0,0,1,1,1,1,],
 [1,1,1,1,1,1,1,1,]]

E=[[0,0,0,0,0,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,0,0,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,0,0,0,0,1,1,1,],
 [1,1,1,1,1,1,1,1,]]

F=[[0,0,0,0,0,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,0,0,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [1,1,1,1,1,1,1,1,]]

G=[[1,0,0,0,1,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,1,1,1,1,],
 [0,1,0,0,1,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [1,0,0,0,1,1,1,1,],
 [1,1,1,1,1,1,1,1,]]

H=[[0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,0,0,0,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [0,1,1,1,0,1,1,1,],
 [1,1,1,1,1,1,1,1,]] 

I=[[1,0,0,0,1,1,1,1,],
 [1,1,0,1,1,1,1,1,],
 [1,1,0,1,1,1,1,1,],
 [1,1,0,1,1,1,1,1,],
 [1,1,0,1,1,1,1,1,],
 [1,1,0,1,1,1,1,1,],
 [1,0,0,0,1,1,1,1,],
 [1,1,1,1,1,1,1,1,]] 

J=[[1,1,1,1,0,1,1,1,],
[1,1,1,1,0,1,1,1,],
[1,1,1,1,0,1,1,1,],
[1,1,1,1,0,1,1,1,],
[1,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,0,0,0,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

K=[[0,1,1,1,0,1,1,1,],
[0,1,1,0,1,1,1,1,],
[0,1,0,1,1,1,1,1,],
[0,0,1,1,1,1,1,1,],
[0,1,0,1,1,1,1,1,],
[0,1,1,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

L=[[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,0,0,0,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

M=[[0,1,1,1,0,1,1,1,],
[0,0,1,0,0,1,1,1,],
[0,1,0,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

N=[[0,1,1,1,0,1,1,1,],
[0,0,1,1,0,1,1,1,],
[0,1,0,1,0,1,1,1,],
[0,1,1,0,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

O=[[1,0,0,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,0,0,0,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

P=[[0,0,0,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,0,0,0,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

Q=[[1,0,0,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,0,1,0,1,1,1,],
[0,1,1,0,0,1,1,1,],
[1,0,0,0,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

R=[[0,0,0,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,0,0,0,1,1,1,1,],
[0,1,0,1,1,1,1,1,],
[0,1,1,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

S=[[1,0,0,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,1,1,1,1,],
[1,0,0,0,1,1,1,1,],
[1,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,0,0,0,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

T=[[0,0,0,0,0,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

V=[[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,0,1,0,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

W=[[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,0,1,0,1,1,1,],
[1,0,1,0,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

X=[[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,0,1,0,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,0,1,0,1,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

Y=[[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[0,1,1,1,0,1,1,1,],
[1,0,1,0,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,1,1,1,1,1,1,1,]]

Z=[[0,0,0,0,0,1,1,1,],
[1,1,1,1,0,1,1,1,],
[1,1,1,0,1,1,1,1,],
[1,1,0,1,1,1,1,1,],
[1,0,1,1,1,1,1,1,],
[0,1,1,1,1,1,1,1,],
[0,0,0,0,0,1,1,1,],
[1,1,1,1,1,1,1,1,]]

word=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,V,W,X,Y,Z]
while True:
    for letter in word:
      timeout=1 #seconds
      timeout_start = time.time()
      while(time.time()<timeout_start+timeout):
        printCharacter(letter)
   
GPIO.cleanup()
