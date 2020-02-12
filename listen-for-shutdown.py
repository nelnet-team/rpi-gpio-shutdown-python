#!/usr/bin/env python3


import RPi.GPIO as GPIO
import subprocess
import os
import sys

pin=21 # GPIO number, not pin number
direction="FALLING"

if len(sys.argv) > 1:
    pin=sys.argv[1]
elif "ENV_GPIO" in os.environ:
    pin=os.getenv("ENV_GPIO")

if len(sys.argv) > 2:
    direction=sys.argv[2]
elif "ENV_DIRECTION" in os.environ:
    direction=os.getenv("ENV_DIRECTION")

print ("Waiting for {} on GPIO pin {}".format(direction,str(pin)))

GPIO.setmode(GPIO.BCM)

if direction=="RISING":
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.wait_for_edge(pin, GPIO.RISING)
else:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.wait_for_edge(pin, GPIO.FALLING)

subprocess.call(['shutdown', '-p', 'now'], shell=False)

