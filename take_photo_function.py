# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Packages to install on Picamera
import time
import picamera 
import numpy as np
def takePhoto():
    print(np.__version__)
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('face.jpg')


#runs the code
takePhoto();