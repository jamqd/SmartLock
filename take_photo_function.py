# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Packages to install on Picamera
import time
import datetime
import picamera 
from light_up_leds import light_up_leds
    
def takePhoto():
    blinker = light_up_leds()
    currentDT = datetime.datetime.now()
    name = str(int(time.time()))+".jpg"

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        blinker.blink('white',3,0.5)
        camera.capture('/home/pi/Desktop/SmartLock/images/'+name)
    return name



        
