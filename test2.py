#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 02:13:43 2019

@author: melodychen
"""

import RPi.GPIO as GPIO
import time
LockPin = 7
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LockPin, GPIO.OUT)
    GPIO.output(LockPin, GPIO.LOW)
def lock():
    GPIO.output(LockPin, GPIO.HIGH)
    #time.sleep(10)
def unlock():
    GPIO.output(LockPin, GPIO.LOW)
    #time.sleep(1)
def destroy():
    GPIO.output(LockPin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        lock()
    except KeyboardInterrupt:
        destroy()