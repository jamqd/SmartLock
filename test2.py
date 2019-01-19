#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 02:13:43 2019

@author: melodychen
"""

import RPi.GPIO as GPIO
import time
LedPin = 7
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.LOW)
def lock():
    GPIO.output(LedPin, GPIO.HIGH)
    time.sleep(10)
def unlock():
    GPIO.output(LedPin, GPIO.LOW)
    time.sleep(1)
def destroy():
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        lock()
    except KeyboardInterrupt:
        destroy()