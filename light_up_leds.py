#defining the RPi's pins as Input / Output
import RPi.GPIO as GPIO

#importing the library for delaying command.
import time 

class light_up_leds:
    def __init__(self):
        try:
            #used for GPIO numbering
            GPIO.setmode(GPIO.BOARD) 
            #defining the pins
            self.green = 13
            self.red = 11
            self.blue = 15

            #defining the pins as output
            GPIO.setup(self.red, GPIO.OUT) 
            GPIO.setup(self.green, GPIO.OUT)
            GPIO.setup(self.blue, GPIO.OUT)
        except:
            GPIO.cleanup()
        

    def lightBlue(self): #blue 11
        try:
            GPIO.output(self.green, GPIO.HIGH)
            GPIO.output(self.red, GPIO.HIGH)
            GPIO.output(self.blue, GPIO.LOW)
        
        except: 
            # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
            GPIO.cleanup()
            

    def lightGreen(self): #Green
        try:
            GPIO.output(self.green, GPIO.LOW)
            GPIO.output(self.red, GPIO.HIGH)
            GPIO.output(self.blue, GPIO.HIGH)
            
        except: 
            # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
            GPIO.cleanup()

    def lightRed(self): #red
        try:
            GPIO.output(self.green, GPIO.HIGH)
            GPIO.output(self.red, GPIO.LOW)
            GPIO.output(self.blue, GPIO.HIGH)
        except: 
            GPIO.cleanup()
            
    def lightPurple(self): #blue
        try:
            GPIO.output(self.green, GPIO.HIGH)
            GPIO.output(self.red, GPIO.LOW)
            GPIO.output(self.blue, GPIO.LOW)
        
        except: 
            # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
            GPIO.cleanup()
    def lightYellow(self):
        try:
            GPIO.output(self.green, GPIO.LOW)
            GPIO.output(self.red, GPIO.LOW)
            GPIO.output(self.blue, GPIO.HIGH)
        
        except: 
            # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
            GPIO.cleanup()
    def lightLBlue(self):
        try:
            GPIO.output(self.green, GPIO.LOW)
            GPIO.output(self.red, GPIO.HIGH)
            GPIO.output(self.blue, GPIO.LOW)
        
        except: 
            # the purpose of this part is, when you interrupt the code, it will stop the while loop and turn off the pins, which means your LED won't light anymore
            GPIO.cleanup()
    def lightWhite(self):
        try:
            GPIO.output(self.green, GPIO.LOW)
            GPIO.output(self.red, GPIO.LOW)
            GPIO.output(self.blue, GPIO.LOW)
        except: 
            GPIO.cleanup()
    def blink(self,color, blinks, interval):
        try:
            for x in range(0, blinks):
                if color == 'white':
                    self.lightWhite()
                elif color == 'red':
                    self.lightRed()
                elif color == 'green':
                    self.lightGreen()
                elif color == 'blue':
                    self.lightBlue()
                elif color =='purple':
                    self.lightPurple()
                elif color =='lightBlue':
                    self.lightLBlue()
                time.sleep(interval/2)
                self.off()
                time.sleep(interval/2)
        except:
            GPIO.cleanup()
    def destroy(self):
        GPIO.cleanup()
        print("destroying")
    def off(self):
        try:
            GPIO.output(self.green, GPIO.HIGH)
            GPIO.output(self.red, GPIO.HIGH)
            GPIO.output(self.blue, GPIO.HIGH)
        except KeyboardInterrupt: 
            GPIO.cleanup()

#a = light_up_leds()
#a.blink('red',3, 1)
#a.blink('green',3, 1)
#a.blink('blue',3, 1)
#a.blink('white',3, 1)
#a.blinkWhite(3, 0.5)
#a.lightRed()
#time.sleep(1)
#a.off()
#a.lightRed()
#time.sleep(1)
#time.sleep(2)
#a.lightGreen()
#time.sleep(2)
#a.lightBlue()
#time.sleep(2)
#a.lightLBlue()
#time.sleep(2)
#a.lightPurple()
#time.sleep(2)
#a.lightYellow()
#time.sleep(2)
#a.lightWhite()
#time.sleep(5)
#
##a.lightBlue()
##time.sleep(10)
#
#GPIO.cleanup()
