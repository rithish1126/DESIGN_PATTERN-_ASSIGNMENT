import time
from abc import ABC, abstractmethod

class WeatherStation_class:
    def __init__(self):
        # List to store registered observers
        self.observers = []  
        # Variable to track previous weather data
        self.previous_weather_data = None  

    def register_observers(self, observer):
        # Add an observer to the list of registered observers
        self.observers.append(observer)  

    def unregister_observer(self, observer):
        # Remove an observer from the list of registered observers
        self.observers.remove(observer)  

    def notify_observers(self, weather_data):
        for observer in self.observers:
            # Notify each observer by calling their update method with the weather data
            observer.update(weather_data)  

    def get_weather_data(self):
        temperature = 60
        humidity = 46
        pressure = 599
        return {'temperature': temperature, 'humidity': humidity, 'pressure': pressure}  # Simulated method to fetch weather data

    def start_monitoring(self):
        # Run indefinitely
        while True: 
            weather_data = self.get_weather_data()  # Get the current weather data
            if weather_data != self.previous_weather_data:  # Check if the weather data has changed
                self.notify_observers(weather_data)  # Notify the observers about the updated weather data
                self.previous_weather_data = weather_data  # Update the previous weather data
            # Delay between iterations (5 seconds)
            time.sleep(5)  

class DisplayDevice(ABC):
    @abstractmethod
    # Abstract method to be implemented by the subclasses
    def update(self, weather_data):
        pass  
# Mobile display class
class MobileDisplay(DisplayDevice):
    def update(self, weather_data):
        print("there is an update on the weather")
        print("Mobile Display:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Pressure: {weather_data['pressure']}")

# Web display class
class WebDisplay(DisplayDevice):
    def update(self, weather_data):
        print("there is an update on the weather")
        print("Web Display:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Pressure: {weather_data['pressure']}")

#Desktop Display class
class DesktopDisplay(DisplayDevice):
    def update(self, weather_data):
        print("there is an update on the weather")
        print("Desktop Display:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Humidity: {weather_data['humidity']}")
        print(f"Pressure: {weather_data['pressure']}")


if __name__ == '__main__':
    weather_station = WeatherStation_class()

    mobile_app_display = MobileDisplay()
    web_interface_display = WebDisplay()
    desktop_application_display = DesktopDisplay()

    weather_station.register_observers(mobile_app_display)  # Register the mobile app display device
    weather_station.register_observers(web_interface_display)  # Register the web interface display device
    weather_station.register_observers(desktop_application_display)  # Register the desktop application display device

    weather_station.start_monitoring()  # Start monitoring the weather data
