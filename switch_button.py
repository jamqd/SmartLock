#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 02:40:52 2019

@author: melodychen
"""

import RPi.GPIO as GPIO
import time
from motion_detect import motion_detect

def button_pressed():
    md = motion_detect()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    count = 0
    m_count = 0
    while True:
        if(count%10==0):
            md.sample()
            dist = md.calcDist()
            if dist > 10:
                print(dist)
                m_count += 1
        input_state1 = GPIO.input(37)
        input_state2 = GPIO.input(16)
        if (input_state1 == False or input_state2 == False or dist>150):
            if(input_state1 == False):
                print('Button 1 Pressed')
                time.sleep(0.2)
                return 1
            if (input_state2 == False):
                print('Button 2 Pressed')
                time.sleep(0.2)
                return 2
            if (dist > 150):
                return 0
        count += 1
def test_button2_was_pressed():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        input_state = GPIO.input(16)
        if (input_state == False):
            print('Button 2 Pressed')
            time.sleep(0.2)
            return True

            