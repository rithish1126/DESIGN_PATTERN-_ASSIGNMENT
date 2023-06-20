# DESIGN_PATTERN-_ASSIGNMENT

# Task 1

Design and implement a weather monitoring system in Python that notifies multiple display
devices when the weather conditions change. Implement the suitable design pattern to
establish a one-to-many relationship between the weather station (subject) and the display
devices (observers). When the weather data is updated, all registered display devices should be
notified and display the latest weather information.

- Weather station collects and stores weather data.
- Multiple display devices (Mobile Display, Web Display, and Desktop Display) can subscribe to the weather station for real-time updates.
- When new weather data is available, the weather station automatically notifies all registered display devices.
- Each display device is responsible for updating its own user interface and displaying the received weather data.
- The system allows new display devices to be added without modifying the existing code of the weather station or other display devices.
- Display devices have the flexibility to unsubscribe from the weather station if they no longer wish to receive updates.
<img width="789" alt="Screenshot 2023-06-20 at 5 07 18 PM" src="https://github.com/rithish1126/DESIGN_PATTERN-_ASSIGNMENT/assets/122535424/11d38891-7dea-4ed2-b43a-498641d2e244">

# Task 2

Design and implement a vehicle manufacturing system in Python that utilizes the suitable
design pattern to create different types of vehicles. The system should allow users to specify
the type of vehicle they want to manufacture (car, motorcycle, or truck) and provide the
corresponding factory to create the desired vehicle object. The factory should encapsulate the
vehicle creation logic, ensuring that the correct type of vehicle is created based on the user's
input.

## Classes
- **Vehicle_class (Abstract Product):** Represents the abstract class for a vehicle with the `get_details()` abstract method.

- **Car_class (Concrete Product):** Represents a car with specific properties like the number of wheels, maximum speed, and seating capacity. It implements the `get_details()` method to provide the car's details.

- **Motorcycle_class (Concrete Product):** Represents a motorcycle with specific properties like the number of wheels and maximum speed. It implements the `get_details()` method to provide the motorcycle's details.

- **Truck_class (Concrete Product):** Represents a truck with specific properties like the number of wheels and maximum speed. It implements the `get_details()` method to provide the truck's details.

- **VehicleFactory_class (Abstract Creator):** Represents the abstract class for the Vehicle Factory. It declares the `create_vehicle()` abstract method to create a specific type of vehicle.

- **CarFactory_class (Concrete Creator):** Represents a concrete creator that creates Car objects. It implements the `create_vehicle()` method to create a Car object with the desired maximum speed and seating capacity.

- **MotorcycleFactory_class (Concrete Creator):** Represents a concrete creator that creates Motorcycle objects. It implements the `create_vehicle()` method to create a Motorcycle object with the desired maximum speed.

- **TruckFactory_class (Concrete Creator):** Represents a concrete creator that creates Truck objects. It implements the `create_vehicle()` method to create a Truck object with the desired maximum speed.
  
<img width="692" alt="Screenshot 2023-06-20 at 5 08 00 PM" src="https://github.com/rithish1126/DESIGN_PATTERN-_ASSIGNMENT/assets/122535424/ecadadbd-d4a4-42ac-b363-8c0cb9c97257">

