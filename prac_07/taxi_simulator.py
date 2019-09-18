"""Taxi simulator"""

from prac_06.car import Car
from prac_07.taxi import Taxi
from prac_07.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():

    bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    userChoice = input(">>> ").lower()
    while userChoice != "q":
        if userChoice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            # no error-checking
            taxiChoice = int(input("Choose taxi: "))
            current_taxi = taxis[taxiChoice]
        elif userChoice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            tripCost = current_taxi.get_fare()
            print("Your {0} trip cost you ${1}".format(current_taxi.name,
                                                         tripCost))
            bill += tripCost
        else:
            print("Invalid option")
        print("Bill to date: ${0}".format(bill))
        print(MENU)
        userChoice = input(">>> ").lower()

    print("Total trip cost: ${0}".format(bill))
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))

def run_tests():
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    distance = int(input("Drive how far? "))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())

main()