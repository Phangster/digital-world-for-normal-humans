from RPi import GPIO
from firebase import firebase
from time import sleep

url= 'https://digital-world-cohort-11.firebaseio.com/'
token = '5eucPr4baUntEEeJ8RHrkHmYLdwUGLCKF5yQb7Fg' 
firebase=firebase.FirebaseApplication(url,token)

GPIO.setmode(GPIO.BCM)
ledcolor={'yellow':20, 'red':21}

GPIO.setup(ledcolor.values(), GPIO.OUT)

def set_led(ledno, status):
	# you can use this to set the LED on or off
	pass

while True:
	print (firebase.get('/yellow'))
	print (firebase.get('/red'))
	if firebase.get('/yellow'):
		GPIO.output(ledcolor['yellow'], GPIO.HIGH)
	else:
		GPIO.output(ledcolor['yellow'], GPIO.LOW)
	if firebase.get('/red'):
		GPIO.output(ledcolor['red'], GPIO.HIGH)
	else:
		GPIO.output(ledcolor['red'], GPIO.LOW)
	sleep(1)
    
