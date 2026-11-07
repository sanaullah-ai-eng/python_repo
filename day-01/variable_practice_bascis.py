"""
Question : 01 
 Take a Number as input print weither its even or odd 
 using the modulue % opertor and comparision operator """

user_input=int(input("Enter Your Number : "))
# result = user_input % 2

print(user_input % 2 == 0 )
print("/n")




"""
Question : 02 
 Take user age as input check and print weither they are eligible to vote 
 (age>=18) and  wither they are senior citizen (age>=60)
 print both results """

user_age = int(input("Enter Your Age : "))

print(f"{user_age>=18} You are eligible for vote")
print(f"{user_age>=60} You are senior citizen")
print("/n")


"""
Question : 03 
 Take Two Number input from the user and print their
 sum
 Difference
 product and
 Reminder """

user_input1=int(input("Enter Your First Number :"))
user_input2=int(input("Enter Your Second Number :")) 
sum = user_input1+user_input2
difference=user_input1-user_input2
product=user_input1*user_input2
reminder=user_input1%user_input2
print(f"Sum is {sum}")
print(f"Difference : is {difference}")
print(f"Product is : {product}")
print(f"reminder is : {reminder}")
print("/n")
print("/n")


"""
Question : 04 
 Student score marks in 3 sbjects 
 Take all three as input
 calculate average and total and print using f string """

score1=int(input("Enter Marks 1 : "))
score2=int(input("Enter Marks 2 : "))
score3=int(input("Enter Marks 3 : "))

total=score1+score2+score3
avg = (score1+score2+score3)/3
print(f"Your Total marks is {total} and average is {avg}")
print("/n")


