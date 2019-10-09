"""silver_service_taxi_test.py"""

from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi"""
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(19)
    print(taxi)
    print(taxi.get_fare())

main()
