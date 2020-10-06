import RPi.GPIO as GPIO
from time import sleep
from time import time
def printDig(dig):
    if dig==1:
        GPIO.output([D1,D2,D3,D4],[False,True,True,True])
    elif dig==2:
        GPIO.output([D1,D2,D3,D4],[True,False,True,True])
    elif dig==3:
        GPIO.output([D1,D2,D3,D4],[True,True,False,True])
    elif dig==4:
        GPIO.output([D1,D2,D3,D4],[True,True,True,False])
    sleep(0.001)
    GPIO.output([D1,D2,D3,D4],[True,True,True,True])
def printDigVal(dig,val):
    if val=='0':
        print0()
    if val=='1':
        print1()
    if val=='2':
        print2()
    if val=='3':
        print3()
    if val=='4':
        print4()
    if val=='5':
        print5()
    if val=='6':
        print6()
    if val=='7':
        print7()
    if val=='8':
        print8()
    if val=='9':
       print9()
    printDig(dig)

def print0():
    GPIO.output([a,b,c,d,e,f,g],[True,True,True,True,True,True,False])
    #GPIO.output(DP,True)
def print1():
    GPIO.output([a,b,c,d,e,f,g],[False,True,True,False,False,False,False])
    #GPIO.output(DP,True)
def print2():
    GPIO.output([a,b,c,d,e,f,g],[True,True,False,True,True,False,True])
    #GPIO.output(DP,True)
def print3():
    GPIO.output([a,b,c,d,e,f,g],[True,True,True,True,False,False,True])
    #GPIO.output(DP,True)
def print4():
    GPIO.output([a,b,c,d,e,f,g],[False,True,True,False,False,True,True])
    #GPIO.output(DP,True)
def print5():
    GPIO.output([a,b,c,d,e,f,g],[True,False,True,True,False,True,True])
    #GPIO.output(DP,True)
def print6():
    GPIO.output([a,b,c,d,e,f,g],[True,False,True,True,True,True,True])
    #GPIO.output(DP,True)
def print7():
    GPIO.output([a,b,c,d,e,f,g],[True,True,True,False,False,False,False])
    #GPIO.output(DP,True)
def print8():
    GPIO.output([a,b,c,d,e,f,g],[True,True,True,True,True,True,True])
    #GPIO.output(DP,True)
def print9():
    GPIO.output([a,b,c,d,e,f,g],[True,True,True,True,False,True,True])
    #GPIO.output(DP,True)
GPIO.setmode(GPIO.BOARD)
a=7
b=12
c=18
d=15
e=13
f=11
g=22
DP=16
D1=29
D2=31
D3=32
D4=33
GPIO.setup([a,b,c,d,e,f,g],GPIO.OUT)
GPIO.setup(DP,GPIO.OUT)
GPIO.setup([D1,D2,D3,D4],GPIO.OUT)
v1,V2,V3,V4='','','',''
for i in range(0, 10000):
    it=str(i)
    timeout=.1 #seconds
    timeout_start = time()
    while(time()<timeout_start+timeout):
        if len(it)==1:
            v1=it[0]
            printDigVal(4,v1)
        if len(it)==2:
            v1=it[0]
            v2=it[1]
            printDigVal(3,v1)
            printDigVal(4,v2)
        if len(it)==3:
            v1=it[0]
            v2=it[1]
            v3=it[2]
            printDigVal(2,v1)
            printDigVal(3,v2)
            printDigVal(4,v3)
        if len(it)==4:
            v1=it[0]
            v2=it[1]
            v3=it[2]
            v4=it[3]
            printDigVal(1,v1)
            printDigVal(2,v2)
            printDigVal(3,v3)
            printDigVal(4,v4)

GPIO.cleanup()

