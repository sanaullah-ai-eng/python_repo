class Vehicle:
    def __init__(self, brand: str) -> None:
        print("This is vehicle constructor")
        self.brand = brand


class Car(Vehicle):
    def __init__(self, fuel: str, brand: str) -> None:
        print("This is car constructor")
        super().__init__(brand)
        self.fuel = fuel

    def display(self):
        print(f"You have a {self.brand} car with {self.fuel} type")


car = Car("petrol", "maruti")
car.display()


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model


class ElectricCar(Vehicle):
  def __init__(self, brand, model, battery_size):
    # Call the parent class's __init__ to set brand and model
    super().__init__(brand, model)
    # Set the child-specific attribute
    self.battery_size = battery_size


my_car = ElectricCar("Tesla", "Model 3", "75 kWh")
print(my_car.brand)  # Output: Tesla
print(my_car.battery_size)  # Output: 75 kWh
