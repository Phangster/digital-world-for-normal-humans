from pythymiodw import *
from time import sleep
from firebase import firebase

url = "https://digital-world-cohort-4.firebaseio.com/" # URL to Firebase database
token = '3ZPgzzzMpnbUUIRxf1kyiNsD5T5Zy9FF9UqgBL5a' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

r = ThymioReal() # create an eBot object

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

r=ThymioReal()

for i in range (1):
    forward(r,100,3)
    mech.wheels(0,0)
    right(r)

no_movements = True
mech.quit()
# while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)




