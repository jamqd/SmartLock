import RPi.GPIO as GPIO
import time
LedPin = 7
locked = False;
#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH) #LOCKS IT
lock = True
def lock():
    lock = True
    GPIO.output(LedPin, GPIO.LOW)
def unlock():
    lock = False
    GPIO.output(LedPin, GPIO.HIGH)
    time.sleep(1)
    print("unlock")    
def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()
#if __name__ == '__main__':
#    try:
#        setup()
#        unlock()
#        lock()
#    except KeyboardInterrupt:
#        print ("\n")
#    except:
#        print ("Other error")
#    finally:
#        GPIO.cleanup()




