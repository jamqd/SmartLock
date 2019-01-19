#defining the RPi's pins as Input / Output
import RPi.GPIO as GPIO

#importing the library for delaying command.
import time 

#used for GPIO numbering
GPIO.setmode(GPIO.BCM) 

#closing the warnings when you are compiling the code
GPIO.setwarnings(False)

RUNNING = True

#defining the pins
green = 20
red = 22
blue = 21

#defining the pins as output
GPIO.setup(red, GPIO.OUT) 
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

#choosing a frequency for pwm
Freq = 100


def lightBlue():
    try:
        #we are starting with the loop
        while True:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(blue, GPIO.LOW)
        
    except KeyboardInterrupt: 
        # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
        RUNNING = False  
        GPIO.cleanup()

def lightRed():
    try:
        #we are starting with the loop
        while True:
            GPIO.output(green, GPIO.LOW)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.HIGH)
        
    except KeyboardInterrupt: 
        # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
        RUNNING = False  
        GPIO.cleanup()

def lightGreen():
    try:
        #we are starting with the loop
        while True:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(red, GPIO.LOW)
            GPIO.output(blue, GPIO.LOW)
        
    except KeyboardInterrupt: 
        # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
        RUNNING = False  
        GPIO.cleanup()

