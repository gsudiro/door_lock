import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [21]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    SleepTimeL = 2

try:
    GPIO.output(21, GPIO.LOW)
    print ("ONE")
    time.sleep(SleepTimeL);
    GPIO.cleanup()
    print ("GOOD BYE")

except KeyboardInterrupt:
    print ("QUIT")

GPIO.cleanup()