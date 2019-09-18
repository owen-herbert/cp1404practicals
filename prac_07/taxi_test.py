"""Taxi Test"""

from prac_07.taxi import Taxi

def main():
    """Test Class for taxi"""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)