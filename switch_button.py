#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 02:40:52 2019

@author: melodychen
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def test_button_was_pressed():

    while True:
        input_state = GPIO.input(37)
        if (input_state == False):
            print('Button Pressed')
            time.sleep(0.2)
            return True

            