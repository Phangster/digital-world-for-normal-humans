import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase

url = "https://internet-of-things-c572e.firebaseio.com/" 
token = 'qcHr20bWwg1ziqik58l39JD8UlcLLIGa8HJ0DaSC' 

firebase = firebase.FirebaseApplication(url, token)

# Use the BCM GPIO numbers as the numbering scheme.
GPIO.setmode(GPIO.BCM)

# Use GPIO12, 16, 20 and 21 for the buttons.
s1 = 12
s2 = 16
s3 = 20
s4 = 21
switch_list = [12, 16, 20, 21]
# Set GPIO numbers in the list: [12, 16, 20, 21] as input with pull-down resistor.

movement_list = []

GPIO.setup(switch_list, GPIO.IN, GPIO.PUD_DOWN)

done = False

while done == False:
    if GPIO.input(12) == GPIO.HIGH:
        movement_list.append('left')
        print('Left added.')
        
        sleep(0.1)
        
    elif GPIO.input(16) == GPIO.HIGH:
        movement_list.append('right')
        print('Right added.')
        sleep(0.1)
    elif GPIO.input(20) == GPIO.HIGH:
        movement_list.append('up')
        print('Up added.')
        sleep(0.1)
    elif GPIO.input(21) == GPIO.HIGH:
        movement_list.append('done')
        print('Terminating control, uploading sequence to Firebase.')
        firebase.put('/','movement_list', movement_list)
        done = True
        break
    
while done==True:
    a=firebase.get('/movement_list') # get the value from node age
    if a == None:
        done=False
    sleep(0.5)

    # Write your code here

    '''
    We loop through the key (button name), value (gpio number) pair of the buttons
    dictionary and check whether the button at the corresponding GPIO is being
    pressed. When the OK button is pressed, we will exit the while loop and 
    write the list of movements (movement_list) to the database. Any other button
    press would be stored in the movement_list.

    Since there may be debouncing issue due to the mechanical nature of the buttons,
    we can address it by putting a short delay between each iteration after a key
    press has been detected.
    '''


# Write to database once the OK button is pressed

