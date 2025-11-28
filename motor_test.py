import RPi.GPIO as GPIO
import time

# === Pin definitions (BCM) ===
DIR_PIN  = 17   # A4988 DIR
STEP_PIN = 18   # A4988 STEP
EN_PIN   = 23   # A4988 EN (LOW = enabled). Tie to Pi if you want software enable.

STEP_DELAY = 0.001   # seconds between STEP edges (1 ms -> ~500 steps/sec)
STEP_COUNT = 800     # number of steps each way

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(EN_PIN, GPIO.OUT)

def do_steps(direction_high, steps, delay):
    """direction_high: True for DIR=HIGH, False for DIR=LOW"""
    GPIO.output(DIR_PIN, GPIO.HIGH if direction_high else GPIO.LOW)
    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    # Disable at start (outputs off)
    GPIO.output(EN_PIN, GPIO.HIGH)

    # Enable driver
    GPIO.output(EN_PIN, GPIO.LOW)
    time.sleep(0.05)

    print("Forward...")
    do_steps(direction_high=True, steps=STEP_COUNT, delay=STEP_DELAY)

    time.sleep(0.5)

    print("Backward...")
    do_steps(direction_high=False, steps=STEP_COUNT, delay=STEP_DELAY)

    # Turn driver off at the end so it stops drawing current
    GPIO.output(EN_PIN, GPIO.HIGH)

finally:
    GPIO.cleanup()
