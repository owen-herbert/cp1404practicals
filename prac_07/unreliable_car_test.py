"""Test the unreliable car"""

from prac_07.unreliable_car import UnreliableCar

def main():
    """Test class for UnreliableCar"""

    car = UnreliableCar("Unreliable Car", 100, 20)

    for i in range(1, 12):
        print("Driving car {0}km".format(i))
        print("{0} drove {1}km".format(car.name, car.drive(i)))

    print(car)

main()