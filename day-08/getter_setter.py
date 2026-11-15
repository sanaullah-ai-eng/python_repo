class Student : 
    def __init__(self, name:str)->None : 
        self.__name= name 

# Getter 
    def get_name(self):
        return self.__name
# setter 
    def set_name(self , new_name: str):
        self.__name= new_name





s1=Student("sanaullah")
print(s1.get_name())
s1.set_name("afzal")
print(s1.get_name())