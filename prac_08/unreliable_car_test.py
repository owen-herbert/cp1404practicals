"""unreliable_car_test.py"""

from prac_08.unreliable_car import UnreliableCar

def main():
    """Test Unreliable Car"""
    reliable_car = UnreliableCar("Toyota", 100, 88)
    unreliable_car = UnreliableCar("Volkswagen", 100, 13)

    for i in range(1, 10):
        print("Driving two vehicles {0}km:".format(i))
        print("{0} drove {1}km".format(reliable_car.name, reliable_car.drive(i)))
        print("{0} drove {1}km".format(unreliable_car.name, unreliable_car.drive(i)))

    print(reliable_car)
    print(unreliable_car)

main()
