import RPi.GPIO as GPIO
import time
emergency = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
print "EMERGENCY!"
flash = 0
while emergency:
    try:
        GPIO.output(17, GPIO.HIGH)  # RED
        time.sleep(0.25)
        GPIO.output(18, GPIO.HIGH)  # BLUE
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.25)
        GPIO.output(18, GPIO.LOW)
        flash += 1
    except(KeyboardInterrupt, SystemExit):
        GPIO.output(18, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        print("__ALARM DISABLED__")
        raise
GPIO.cleanup()
