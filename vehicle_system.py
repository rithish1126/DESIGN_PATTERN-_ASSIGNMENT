from abc import ABC, abstractmethod

# Product (Vehicle)
class Vehicle_class(ABC):
    @abstractmethod
    def get_details(self):
        pass

# Concrete Products (Car, Motorcycle, Truck)
class Car_class(Vehicle_class):
    def __init__(self, max_speed, seating_capacity):
        self.wheels = 4
        self.max_speed = max_speed
        self.seating_capacity = seating_capacity

    def get_details(self):
        return f"Car Details: Wheels={self.wheels}, Seating Capacity={self.seating_capacity}, Max Speed={self.max_speed}"

class Motorcycle_class(Vehicle_class):
    def __init__(self, max_speed):
        self.wheels = 2
        self.max_speed = max_speed

    def get_details(self):
        return f"Motorcycle Details: Wheels={self.wheels}, Max Speed={self.max_speed}"

class Truck_class(Vehicle_class):
    def __init__(self, max_speed):
        self.wheels = 6
        self.max_speed = max_speed

    def get_details(self):
        return f"Truck Details: Wheels={self.wheels}, Max Speed={self.max_speed}"

# Creator (Vehicle Factory)
class VehicleFactory_class(ABC):
    @abstractmethod
    def create_vehicle(self, max_speed):
        pass

# Concrete Creators (Car Factory, Motorcycle Factory, Truck Factory)
class CarFactory_class(VehicleFactory_class):
    def create_vehicle(self, max_speed):
        seating_capacity = self.get_seating_capacity()
        return Car_class(max_speed, seating_capacity)

    def get_seating_capacity(self):
        seating_type = input("Enter the car seating type (5-seater/7-seater): ")
        if seating_type == "5-seater":
            return 5
        elif seating_type == "7-seater":
            return 7
        else:
            print("Invalid car seating type. Defaulting to 5-seater.")
            return 5

class MotorcycleFactory_class(VehicleFactory_class):
    def create_vehicle(self, max_speed):
        return Motorcycle_class(max_speed)

class TruckFactory_class(VehicleFactory_class):
    def create_vehicle(self, max_speed):
        return Truck_class(max_speed)

# Usage
if __name__ == '__main__':
    # User input for the desired vehicle type
    vehicle_type = input("Enter the vehicle type (car/motorcycle/truck): ")

    # User input for the maximum speed
    max_speed = int(input("Enter the maximum speed: "))

    # Vehicle factory based on user input
    if vehicle_type == "car":
        factory = CarFactory_class()
    elif vehicle_type == "motorcycle":
        factory = MotorcycleFactory_class()
    elif vehicle_type == "truck":
        factory = TruckFactory_class()
    else:
        print("Invalid vehicle type.")
        exit()

    # Create the desired vehicle object using the factory
    vehicle = factory.create_vehicle(max_speed)

    # Display the vehicle details
    print(vehicle.get_details())