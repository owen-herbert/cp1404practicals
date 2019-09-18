from prac_07.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()