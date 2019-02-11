#!/usr/bin/env python

#TEST THIS !!!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Shutdown initiated ...')
        time.sleep(0.2)
        from subprocess import call
        call("sudo shutdown -h now", shell=True)
