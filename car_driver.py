#!/usr/bin/python

import RPi.GPIO as GPIO
import time



def run_car():
    mycar = Car()
    mycar.forward(1)
    time.sleep(2)
    mycar.stop()
    time.sleep(1)
    mycar.backword(1)
    time.sleep(2)
    mycar.stop()

class Car():
    def __init__(self):
        self.car_pins=[6,5,13,19,21,12,16,20]
        self.car_wheel4_2 = 5
        self.car_wheel4_1 = 6
        self.car_wheel2_2 = 13
        self.car_wheel2_1 = 19
	self.car_wheel3_1 = 21
	self.car_wheel3_2 = 20
	self.car_wheel1_1 = 16
        self.car_wheel1_2 = 12
        GPIO.setmode(GPIO.BCM)
        for each in self.car_pins:
            GPIO.setup(each, GPIO.OUT)
            GPIO.output(each, 0)

    def forward(self, ns):
        GPIO.output(self.car_wheel3_1, 1)
        GPIO.output(self.car_wheel3_2, 0)
        GPIO.output(self.car_wheel4_1, 1)
        GPIO.output(self.car_wheel4_2, 0)
        GPIO.output(self.car_wheel2_2, 1)
        GPIO.output(self.car_wheel2_1, 0)
        GPIO.output(self.car_wheel1_1, 0)
        GPIO.output(self.car_wheel1_2, 1)

    def stop(self):
        GPIO.output(self.car_wheel3_1, 0)
        GPIO.output(self.car_wheel3_2, 0)
        GPIO.output(self.car_wheel2_1, 0)
        GPIO.output(self.car_wheel2_2, 0)
        GPIO.output(self.car_wheel1_1, 0)
        GPIO.output(self.car_wheel1_2, 0)
        GPIO.output(self.car_wheel4_1, 0)
        GPIO.output(self.car_wheel4_2, 0)
	
    def backword(self, ns):
        GPIO.output(self.car_wheel3_1, 0)
        GPIO.output(self.car_wheel3_2, 1)
        GPIO.output(self.car_wheel4_1, 0)
        GPIO.output(self.car_wheel4_2, 1)
        GPIO.output(self.car_wheel2_2, 0)
        GPIO.output(self.car_wheel2_1, 1)
        GPIO.output(self.car_wheel1_1, 1)
        GPIO.output(self.car_wheel1_2, 0)

if __name__ == '__main__':
    run_car()
