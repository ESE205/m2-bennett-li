import RPi.GPIO as GPIO
import time
from datetime import datetime
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# GPIOs
LED_PIN = 11
SWITCH_PIN = 13
LED_ON = False
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(SWITCH_PIN, GPIO.IN)
SWITCH_STATE = GPIO.input(SWITCH_PIN)

# Command Line
DEBUG = '-debug' in sys.argv
run_time = float(input("Enter the run time: "))
SWITCH_STATE = int(input("Choose a Switch State between 0 and 1: "))
BLICK_RATE = 1 if SWITCH_STATE == 0 else 2

# Helper Functions
def print_debug (start_time, time_left, LED_ON):
	current_time = datetime.fromtimestamp(time.time())
	print(f'Current Time: {current_time} \t Time Left: {time_left:.1f} seconds \t Switch State: {"On" if LED_ON else "Off"}')

# Main
start_time = time.time()
end_time = start_time + run_time

with open ('data.txt', 'w') as data:
   while time.time() < end_time:
      run_time = time.time() - start_time
      SWITCH_STATE = GPIO.input(SWITCH_PIN)
      time_left = end_time - time.time()

      if (SWITCH_STATE == True):
         GPIO.output(LED_PIN, LED_ON)
         LED_ON = not(LED_ON)
         data.write(f'Run Time: {run_time:1.0f}s \t Switch State = {SWITCH_STATE} \n')
         time.sleep(BLICK_RATE)
      if (SWITCH_STATE == False):
         LED_ON = False
         data.write(f'Run Time: {run_time:1.0f}s \t Switch State = {SWITCH_STATE} \n')
         GPIO.output(LED_PIN, LED_ON)
         time.sleep(1)
if (DEBUG) : print_debug(start_time, time_left, LED_ON)
GPIO.cleanup()
