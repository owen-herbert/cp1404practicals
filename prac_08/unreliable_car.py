"""Unreliable Car"""
from prac_08.car import Car
from random import randint

class UnreliableCar(Car):
    """Unreliable car"""

    def __init__(self, name, fuel, reliability):
        """Create an unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven