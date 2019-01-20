import RPi.GPIO as GPIO
import time

#setup
class lock_unlock:
    def __init__(self, LedPin):
        self.LedPin = LedPin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.LedPin, GPIO.OUT)
        #GPIO.output(self.LedPin, GPIO.HIGH) #LOCKS IT
        self.is_locked = True
    def lock(self):
        self.is_locked = True
        GPIO.output(self.LedPin, GPIO.LOW)
        time.sleep(1)
    def unlock(self):
        self.is_locked = False
        GPIO.output(self.LedPin, GPIO.HIGH)
        time.sleep(1)
        print("unlock")    
    def destroy(self):
        GPIO.output(self.LedPin, GPIO.LOW)
        GPIO.cleanup()
        print("destroying")
        
        
#if __name__ == '__main__':
#    try:
#        a = lock_unlock(7)
#        a.setup()
#        a.unlock()
#        a.lock()
#    except KeyboardInterrupt:
#        print ("\n")
#    except:
#        print ("Other error")
#    finally:
#        GPIO.cleanup()




