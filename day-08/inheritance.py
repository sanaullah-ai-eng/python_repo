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