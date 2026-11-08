# print number as input and.print it weither it is zero, positive , negitive 
number = int(input('Enter your Number : '))
number2=int(input('Enter your Number : '))
print("\n")
if number==0:
    print("The Number is Zero.")
elif number%2==0 :
    print(f"The {number} is Positive Number.")
elif number%2!=0:
    print(f"The {number} is Negitive Number.")
    print("\n")




"""Take Two Number as input print the greater of the two and if they are equal print both are equal """
if number>number2:
    print(f"{number} is greater then {number2}")
elif number<number2:
    print(f"{number2} is greater then {number}")
elif number==number2:
    print(f"{number}={number2} Both Number are Equal")
else:
    print("Invaid Numbers.")



"""Take a Student marks as input , print their grades based on their scale 
90 and above A 
75 to 89 B
60 to 74 C
40 to 59 D 
Below 40 F

"""
student_number=int(input("Enter Your Marks: "))
if student_number>=90 and student_number<=100:
    print(f"Your grade is A.")
elif student_number>=75 and student_number>=89:
    print("Your Grade is B.")
elif student_number>=60 and student_number<=74:
    print("Your Grade is C.")
elif student_number>=40 and student_number<=59:
    print("Your Grade is D.")
elif student_number>=0 and student_number<=40:
    print("Your Grade is F.")
else:
    print("Invalid number.")


   
"""Take a year as input
 check if it is a leap year a year is a leap year divisable by 4 but not by 100 
unless it also divisable by 400"""

year = int(input("Enter Year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"The {year} is leap year.")
else:
    print("This is not leap year.")



"""
Q11: Take a person's age and whether they have a valid ID (True/False) as input.
They can enter a venue only if they are 18 or older AND have a valid ID.
Print the appropriate message.
"""

person_age=int(input("Enter your Age : "))
valid_id=input("Enter your id is True or False :") =='True'
if person_age >=18 and valid_id==True:
    print("You can enter venue .")
else:
    print("you are ineligible.")



"""
Q12: Take three numbers as input.
Print the largest of the three without using any built-in function."""

num1=int(input("Enter Your Number 1 : "))
num2=int(input("Enter Your Number 2 : "))
num3=int(input("Enter Your Number 3 : "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")





"""
Q13: Take a number as input.
Using the ternary operator, print "Even" or "Odd" in a single line."""

input_number=int(input("Enter a Number : "))
result= "Even Number" if input_number%2==0 else "Odd Number"
print(result)



"""
Q14: A shop gives discounts based on purchase amount:
- Above 5000 -> 20% discount
- Above 2000 -> 10% discount
- Above 1000 -> 5% discount
- 1000 or below -> no discount
"""


Total_amount=int(input("Enter Total Amount : "))
if Total_amount>=5000:
    discount=(Total_amount*20)/100
    discount_amount=Total_amount-discount
    print(f"With dicount your price is {discount_amount}")
elif Total_amount>=2000 and Total_amount<5000:
    discount=(Total_amount*10)/100
    discount_amount=Total_amount-discount
    print(f"With dicount your price is {discount_amount}")
elif Total_amount>=1000 and Total_amount<2000:
    discount=(Total_amount*5)/100
    discount_amount=Total_amount-discount
    print(f"With dicount your price is {discount_amount}")
if Total_amount<1000:
    print("YOu have no discount .")