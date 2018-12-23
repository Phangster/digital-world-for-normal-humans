#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

def print_temp(t_celcius):
    """ calculate t_fahrenheit and print both
    """
    F=(9/5)*t_celcius+32
    print("The temperature in celsius is {} and fahrenheit is {}".format(t_celcius,F))
    pass

def forward(r,speed, duration):
    """ move both wheels for that duration, and stop
    """
    print("Speed={}".format(speed))
    print("Time={}".format(duration))
    r.wheels(speed,speed)
    r.sleep(duration)
    pass

def backward(r,speed, duration):
    """ move both wheels for that duration, and stop
    """
    print("Speed={}".format(speed))
    print("Time={}".format(duration))
    r.wheels(-speed,-speed)
    r.sleep(duration)
    pass

def left(r):
    r.wheels(0,100)
    r.sleep(3.5)
    pass

def right(r):
    r.wheels(100,0)
    r.sleep(4.8)
    pass

# create an object

############### Start writing your code here ################ 

# Prompt user to enter speed and duration of movement

# Move according to the specified speed and duration

# Read temperature in celcius from the sensor and print it

#r=ThymioReal()
#forward(r,100,3)
#print_temp(r.get_temperature())
#r.quit()

########################## end ############################## 

# disconnect the communication

