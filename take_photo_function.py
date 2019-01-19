# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Packages to install on Picamera
import time
import datetime
import picamera 
import numpy as np

    
def takePhoto():
    currentDT = datetime.datetime.now()
    name = str(int(time.time()))+".jpg"

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(3)
        camera.capture('/home/pi/Desktop/SmartLock/images/'+name)
    return name

#runs the code
print(takePhoto())
        
