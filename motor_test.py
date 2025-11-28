import RPi.GPIO as GPIO
import time

IN1 = 23  # GPIO23 (physical pin 16)
IN2 = 24  # GPIO24 (physical pin 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def set_state(label, in1, in2, t=3):
    print(label)
    GPIO.output(IN1, in1)
    GPIO.output(IN2, in2)
    time.sleep(t)

try:
    # Stop
    set_state("STOP (both LOW)", GPIO.LOW, GPIO.LOW, 2)

    # Direction A
    set_state("DIR A (IN1 HIGH, IN2 LOW)", GPIO.HIGH, GPIO.LOW, 3)

    # Stop
    set_state("STOP (both LOW)", GPIO.LOW, GPIO.LOW, 2)

    # Direction B
    set_state("DIR B (IN1 LOW, IN2 HIGH)", GPIO.LOW, GPIO.HIGH, 3)

    # Final stop
    set_state("STOP (both LOW)", GPIO.LOW, GPIO.LOW, 2)

finally:
    GPIO.cleanup()
