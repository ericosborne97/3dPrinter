import RPi.GPIO as GPIO
import time

# BCM pin numbers
DIR_PIN  = 17   # A4988 DIR
STEP_PIN = 18   # A4988 STEP
EN_PIN   = 23   # A4988 EN (optional: only if you wired this to the Pi)

STEP_DELAY = 0.2    # seconds between step edges (VERY SLOW on purpose)
STEP_COUNT = 20     # 20 steps forward, 20 back

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(EN_PIN, GPIO.OUT)   # comment this line out if EN is not wired to Pi

def do_steps(direction_high, steps, delay):
    GPIO.output(DIR_PIN, GPIO.HIGH if direction_high else GPIO.LOW)
    for i in range(steps):
        print("Step", i+1, "DIR =", "HIGH" if direction_high else "LOW")
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(delay)

try:
    # If EN is wired to Pi: disable at start, then enable
    GPIO.output(EN_PIN, GPIO.HIGH)    # comment out if no EN control
    time.sleep(0.05)
    GPIO.output(EN_PIN, GPIO.LOW)     # comment out if no EN control

    print("FORWARD...")
    do_steps(direction_high=True, steps=STEP_COUNT, delay=STEP_DELAY)

    time.sleep(1.0)

    print("BACKWARD...")
    do_steps(direction_high=False, steps=STEP_COUNT, delay=STEP_DELAY)

    # Turn driver off at the end
    GPIO.output(EN_PIN, GPIO.HIGH)    # comment out if no EN control

finally:
    GPIO.cleanup()
