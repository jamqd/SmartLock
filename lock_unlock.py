import RPi.GPIO as GPIO
import time
LedPin = 7
locked = False;
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH) #LOCKS IT
    lock = True
def lock():
    lock = True
    while True:
        GPIO.output(LedPin, GPIO.HIGH)
def unlock():
    lock = False
    while True:
        GPIO.output(LedPin, GPIO.LOW)
def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()


