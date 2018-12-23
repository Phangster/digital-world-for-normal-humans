from pythymiodw import *
from time import sleep
from firebase import firebase

url = 'https://internet-of-things-c572e.firebaseio.com/' # URL to Firebase database
token = 'qcHr20bWwg1ziqik58l39JD8UlcLLIGa8HJ0DaSC' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)



r = ThymioReal() # create an eBot object

no_movements = True

while no_movements:
    a=firebase.get('/movement_list') # get the value from node age
    if a != None:
        no_movements=False
    time.sleep(0.5)
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here

# Write the code to control the eBot here
def forward(duration):
    r.wheels(100,100)
    r.sleep(duration)
    pass

def right(duration):
    r.wheels(100,-100)
    r.sleep(duration)
    pass

def left(duration):
    r.wheels(-100,100)
    r.sleep(duration)
    pass

while no_movements==False:
    for i in a:
        if i == 'up':
            forward(1)
            time.sleep(1)
        elif i=='left':
            left(1)
            time.sleep(1)
        elif i == 'right':
            right(1)
            time.sleep(1)
        elif i == 'done':
            firebase.put('/', 'movement_list', None)
            no_movements=True
            r.quit()
            break
        

