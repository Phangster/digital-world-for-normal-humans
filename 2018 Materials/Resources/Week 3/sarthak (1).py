import RPi.GPIO as GPIO
import time

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED 1, GPIO24 for LED 2 and GPIO18 for switch
led = [23, 24]
switch = 18

# Set the GPIO23 and GPIO24 as output.
GPIO.setup(led, GPIO.OUT)

# Set the GPIO18 as input with a pull-down resistor.
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

def blink(gpio_number, duration):
    '''This function takes in two input: gpio_number and duration. The
    gpio_number specifies the GPIO number which the LED (to be blinked) is
    connected to. The duration is the blink interval in seconds.'''

    # Write your code here
    pass

while True:
    if GPIO.input(switch) == GPIO.HIGH:
        GPIO.output(led[24], GPIO.LOW)
        While True:
            GPIO.output(led[23], GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led[23], GPIO.LOW)
            time.sleep(1)
    elif GPIO.input(switch) == GPIO.LOW:
        GPIO.output(led[23], GPIO.LOW)
        while True:
            GPIO.output(led[24], GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led[24], GPIO.LOW)
            time.sleep(1)

    pass
