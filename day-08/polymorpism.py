class Vehicle:
    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky"

# Polymorphism in action: same method call, different outputs
vehicles = [Car(), Boat(), Plane()]

for v in vehicles:
    print(v.move())
