"""silver_service_taxi.py"""

from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{0} plus flagfall of ${1}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return self.flagfall + super().get_fare()
