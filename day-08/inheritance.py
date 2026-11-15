class Vehichle: 
    def __init__(self , brand:str): 
        self.brand=brand
    def start(self):
        print(f"{self.brand} starting up....")
class car(Vehichle):
    def drive(self):
        print(f"{self.brand} is driving ")

v = car("marvati")
v.drive()
v.start()







print()
# method overridning 
class Animal:
    def speak(self):
        print("Anima is speaking ")

class Dog(Animal):
    def speak(self):
        print("dog is barking ")
d=Dog()
d.speak()
