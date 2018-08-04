import RPi.GPIO as GPIO
import time
import numpy as np


class LEDSequence:

    led_pins = {}
    alt_pins = {}

    def __init__(self,led_pins):
        self.led_pins = led_pins
        self.initialize_lights()
        self.all_hands()

    def initialize_lights(self):
        pins = self.led_pins.values()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)

        for pin in pins:
            GPIO.output(self.led_pins.get("RED"), GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(self.led_pins.get("RED"), GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.LOW)
        for pin in pins:
            GPIO.output(self.led_pins.get("BLUE"), GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(self.led_pins.get("BLUE"), GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.LOW)
        for pin in pins:
            GPIO.output(self.led_pins.get("GREEN"), GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(self.led_pins.get("GREEN"), GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()
        return 0

    def all_hands(self):
        GPIO.setmode(GPIO.BCM)
        for p in self.led_pins.values():
            GPIO.setup(p,GPIO.OUT)
            GPIO.output(p,GPIO.HIGH)
            time.sleep(1)
        sorted_pins = self.led_pins.values().sort()
        for p in self.led_pins.values():
            GPIO.output(p,GPIO.LOW)
            time.sleep(1)
        for p in self.led_pins.values():
            GPIO.output(p,GPIO.HIGH)
        time.sleep(8)
        for p in self.led_pins.values():
            GPIO.output(p,GPIO.LOW)
        GPIO.cleanup()

    def flash_color(self,color,nflashes):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pins.get(color), GPIO.OUT)
        for i in np.arange(0,nflashes,1):
            GPIO.output(self.led_pins.get(color), GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(self.led_pins.get(color), GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(self.led_pins.get(color), GPIO.HIGH)
            time.sleep(0.2)
            GPIO.cleanup()
        return 0


def main():
    pinout = {"RED": 17, "BLUE": 18,"GREEN":20, "YELLOW": 5}
    leds = LEDSequence(pinout)
    leds.flash_color("RED",4)
    leds.flash_color("GREEN",3)
    leds.flash_color("BLUE",2)
    leds.flash_color("YELLOW",1)


if __name__ == "__main__":
    main()