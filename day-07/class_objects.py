class Student:
    def __init__(self, roll_no: int, name: str, gender: str, age: int) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age

    # Methods
    def display_details(self) -> None:
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")


# Object/Instance
student1 = Student(1, "Anirudh", "Male", 88)
student1.display_details()




# 1. Define the Class (Blueprint)
class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Attribute
        self.color = color  # Attribute

    def drive(self):        # Method
        print(f"The {self.color} {self.brand} is driving.")

# 2. Create Objects (Instances)
car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

# 3. Use the Objects
car1.drive()  # Output: The Red Toyota is driving.
car2.drive()  # Output: The Blue Honda is driving.
