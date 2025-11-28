import RPi.GPIO as GPIO
import time

# Using BCM numbering
IN1 = 23  # Connected to L298N IN1
IN2 = 24  # Connected to L298N IN2

GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

def forward():
    # IN1=1, IN2=0 -> one direction
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def backward():
    # IN1=0, IN2=1 -> opposite direction
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

def stop():
    # Both low -> motor off (coast)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

try:
    # Forward 2 seconds
    forward()
    time.sleep(2)

    # Stop briefly
    stop()
    time.sleep(0.5)

    # Backward 2 seconds
    backward()
    time.sleep(2)

    # Stop at the end
    stop()

finally:
    GPIO.cleanup()
