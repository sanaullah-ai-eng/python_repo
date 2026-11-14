class Student():
    def __init__(self , name:str, age:int, marks:list[int])->None:
        self.name:str = name 
        self.age:int = age 
        self.marks:list[int] = marks  # this is like constctor . 
    def total(self):
        return sum(self.marks)

    def avg(self):
        return sum(self.marks)/len(self.marks)

student1 = Student("sana" , 18 , [22,22,22,33,44,55,66])
print(student1.total())
print(student1.avg())