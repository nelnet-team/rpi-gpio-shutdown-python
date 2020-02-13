#!/usr/bin/env python3


import RPi.GPIO as GPIO
import subprocess
import os
import sys

pin=21 # GPIO number, not pin number
direction="FALLING"

if len(sys.argv) > 1:
    pin=int(sys.argv[1])
    print ("Pin {} from command line".format(str(pin)), flush=True)
elif "ENV_GPIO" in os.environ:
    pin=int(os.getenv("ENV_GPIO"))
    print ("Pin {} from environment".format(str(pin)), flush=True)
else:
    print ("Using default pin {}".format(str(pin)), flush=True)

if len(sys.argv) > 2:
    direction=sys.argv[2]
    print ("Detect state {} from command line".format(direction), flush=True)
elif "ENV_STATE" in os.environ:
    direction=os.getenv("ENV_STATE")
    print ("Detect state {} environment".format(direction), flush=True)
else:
    print ("Detect default state {}".format(direction), flush=True)


GPIO.setmode(GPIO.BCM)

if direction=="RISING":
    print ("Waiting for RISING on GPIO pin {}".format(str(pin)), flush=True)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.wait_for_edge(pin, GPIO.RISING)
    print ("Detected state RISING on pin {}".format(str(pin)), flush=True)
else:
    print ("Waiting for FALLING on GPIO pin {}".format(str(pin)), flush=True)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    print ("Detected state FALLING on pin {}".format(str(pin)), flush=True)

print ("GPIO state detected. Shuting down", flush=True)

subprocess.call(['shutdown', '-h', 'now'], shell=False)

sys.exit(0)
