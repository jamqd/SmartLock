import RPi.GPIO as GPIO
import time
LedPin = 7
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
def lock():
    GPIO.output(LedPin, GPIO.HIGH)
    time.sleep(0.25)
def unlock():
    GPIO.output(LedPin, GPIO.LOW)
    time.sleep(0.25)
def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    for x in range(0,5):
        lock()
        unlock()

