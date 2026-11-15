class Student:
    school="The Boys high school"
    def __init__(self, Name: str) -> None:
        self.Name = Name

s1 = Student("afzal")
s2 = Student("sanaullah")
print(s1.Name)
print(s2.Name)
#instance variable
# 
print(Student.school)  # class variable common in every class
Student.school="xyz"   # changing variable values 
print(Student.school)  # printing 


print(s1.school)
Student.school="Govt Model Boys high school"
print(s2.school)




