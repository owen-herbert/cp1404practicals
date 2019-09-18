"""Unreliable Car Class"""

from prac_06.car import Car
from random import randint

class UnreliableCar(Car):
    reliability = float(49.00)

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        randomNum = randint(1, 100)

        if randomNum >= self.reliability:
            distance = 0

        distanceDriven = super().drive(distance)
        return distanceDriven
