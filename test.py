
import RPi.GPIO as GPIO
import time
LockPin = 7
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LockPin, GPIO.OUT)
    GPIO.output(LockPin, GPIO.HIGH)
def blink():
    GPIO.output(LockPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LockPin, GPIO.LOW)
    time.sleep(1)
def destroy():
    GPIO.output(LockPin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()

