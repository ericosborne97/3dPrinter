import RPi.GPIO as GPIO

out1 = 17
out2 = 18
out3 = 27
out4 = 22

GPIO.setmode(GPIO.BCM)
for pin in (out1, out2, out3, out4):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()
