import RPi.GPIO as GPIO
import time

# GPIO pins (BCM numbering)
IN1 = 17  # L298N IN1
IN2 = 18  # L298N IN2
IN3 = 27  # L298N IN3
IN4 = 22  # L298N IN4

GPIO.setmode(GPIO.BCM)
for pin in (IN1, IN2, IN3, IN4):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Full-step sequence (2-phase on)
FULL_STEP_SEQ = [
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 1, 1, 0),
]

def spin_right_for_5s():
    delay = 0.0125          # seconds per microstep
    steps = 100             # full steps
    # Total time ≈ steps * len(seq) * delay = 100 * 4 * 0.0125 = 5 s

    for _ in range(steps):
        for (a1, a2, b1, b2) in FULL_STEP_SEQ:
            GPIO.output(IN1, a1)
            GPIO.output(IN2, a2)
            GPIO.output(IN3, b1)
            GPIO.output(IN4, b2)
            time.sleep(delay)

try:
    print("Spinning right for ~5 seconds...")
    spin_right_for_5s()
finally:
    # Turn everything off
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.cleanup()
