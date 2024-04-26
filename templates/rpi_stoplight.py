#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Setup the GPIO pins
GPIO.setmode(GPIO.BOARD)

# Define pins for the traffic lights
RED = 21   # Pin connected to the red light
YELLOW = 19  # Pin connected to the yellow light
GREEN = 23  # Pin connected to the green light

# Setup each pin as an output
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

# Variable to control whether to print status messages
print_status = False

def light_on(pin):
    GPIO.output(pin, GPIO.HIGH)
    if print_status:
        if pin == RED:
            print("Red light is on")
        elif pin == YELLOW:
            print("Yellow light is on")
        elif pin == GREEN:
            print("Green light is on")

def light_off(pin):
    GPIO.output(pin, GPIO.LOW)
    if print_status:
        if pin == RED:
            print("Red light is off")
        elif pin == YELLOW:
            print("Yellow light is off")
        elif pin == GREEN:
            print("Green light is off")

def sequence_lights():
    for light in [RED, YELLOW, GREEN]:
        light_on(light)
        time.sleep(1)  # Light stays on for 1 second
        light_off(light)
        time.sleep(1)  # Light is off for 1 second

try:
    while True:
        sequence_lights()

except KeyboardInterrupt:
    print("Program stopped manually")
    GPIO.cleanup()  # Clean up GPIO to reset ports used in this session