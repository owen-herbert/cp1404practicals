"""Silver Service Taxi Class"""

from prac_07.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return "{0} plus flagflass of ${1}".format(super().__str(), self.flagfall)

    def fare(self):
        return self.flagfall + super().fare()