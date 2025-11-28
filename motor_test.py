import RPi.GPIO as GPIO
import time

# === CONFIGURATION ===
DIR_PIN   = 20     # GPIO pin connected to DIR on A4988
STEP_PIN  = 21     # GPIO pin connected to STEP on A4988
ENABLE_PIN = 16    # optional — enable pin on A4988 (if you wire it)
MS1_PIN = 14       # optional — microstep setting pins
MS2_PIN = 15
MS3_PIN = 18

# Number of steps per revolution depends on your motor + microstep setting
STEPS_PER_REV = 200   # adjust to your motor’s full‑step count
DELAY = 0.002         # step pulse delay (seconds) — adjust for speed

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.setup(MS1_PIN, GPIO.OUT)
GPIO.setup(MS2_PIN, GPIO.OUT)
GPIO.setup(MS3_PIN, GPIO.OUT)

# MICROSTEP SETTINGS — e.g. full‑step, half‑step, quarter‑step, etc.
# For example: full‑step:
GPIO.output(MS1_PIN, False)
GPIO.output(MS2_PIN, False)
GPIO.output(MS3_PIN, False)

def step(steps, direction):
    GPIO.output(DIR_PIN, direction)
    GPIO.output(ENABLE_PIN, False)  # enable driver (active LOW on many modules)
    for _ in range(steps):
        GPIO.output(STEP_PIN, True)
        time.sleep(DELAY)
        GPIO.output(STEP_PIN, False)
        time.sleep(DELAY)
    # optionally disable driver after movement
    GPIO.output(ENABLE_PIN, True)

try:
    while True:
        # Rotate one revolution forward
        step(STEPS_PER_REV, True)
        time.sleep(0.5)
        # Rotate one revolution back
        step(STEPS_PER_REV, False)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
