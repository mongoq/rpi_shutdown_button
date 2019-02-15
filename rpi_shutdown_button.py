#!/usr/bin/env python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Shutdown initiated ...')
        from subprocess import call
        call("shutdown -h now", shell=True)
