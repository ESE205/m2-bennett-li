import RPi.GPIO as GPIO
import time
from datetime import datetime
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# board
switch_pin = 13
led_pin = 11
led_on = False
GPIO.setup(switch_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT, initial = GPIO.LOW)
switch_state = GPIO.input(switch_pin)

# command line
while (True):
   switch_state = GPIO.input(switch_pin)
   if (switch_state == True):
      led_on = True
      GPIO.output(led_pin, GPIO.HIGH)
   if (switch_state == False):
      led_on = False
      GPIO.output(led_pin, GPIO.LOW)

GPIO.cleanup()

# main
