import RPi.GPIO as GPIO
import time

# CHANGE THESE to the pins you want (BCM numbers)
PIN1 = 17
PIN2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)

try:
    print(f"Pins {PIN1} and {PIN2} set HIGH. Press Ctrl+C to exit.")
    while True:
        time.sleep(1)  # do nothing, just keep pins high
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
