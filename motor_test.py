import RPi.GPIO as GPIO
import time

# ==== SET THESE TO YOUR WIRING (BCM NUMBERS) ====
DIR_PIN  = 17   # GPIO connected to A4988 DIR
STEP_PIN = 18   # GPIO connected to A4988 STEP
# ===============================================

STEP_DELAY = 0.001   # seconds between step edges (1 ms)
STEP_COUNT = 800     # number of steps to move

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

# Optional: make sure EN pin on A4988 is LOW (enabled)
# If you wired EN to a Pi pin, set it up & drive it LOW here.
# If EN is tied to GND on the board, you can ignore this.

try:
    # ---- Move in one direction ----
    print("Moving forward...")
    GPIO.output(DIR_PIN, GPIO.HIGH)   # direction (change HIGH/LOW to reverse)

    for _ in range(STEP_COUNT):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(STEP_DELAY)

    print("Done.")

finally:
    GPIO.cleanup()
