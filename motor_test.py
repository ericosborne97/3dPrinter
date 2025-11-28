import RPi.GPIO as GPIO
import time

PIN1 = 2   # GPIO2 (physical pin 3)
PIN2 = 3   # GPIO3 (physical pin 5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(PIN2, GPIO.OUT, initial=GPIO.HIGH)

try:
    print(f"Pins {PIN1} and {PIN2} set HIGH. Press Ctrl+C to exit.")
    while True:
        time.sleep(1)  # keep pins high
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
