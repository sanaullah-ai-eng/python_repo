def greet(name,age):
    return(f"your name is {name} and age is {age}")
data=greet("sanaullah" , 18)
print(data)


# if number is prime true and if the number is not prime false 

def is_prime(num):
    count=0
    for i in range(1,1+num):
        if num%i==0:
            count+=1
    if count==2 :
        return True
    else:
        return False

print(is_prime(20))





#Question 
#write a function name sqaure that take a number and return its square store the result and print it ..
def square(number):
    return number*number
result=square(20)
print(result)



#Question 
# write a function  that called min_of_three and take three numbers and return the smallest without using any build in function 
def min_of_three(num1,num2,num3):
    if num1<num2 and num1<num3:
        return num1
    elif num2<num1 and num2<num3:
        return num2
    return num3
minimum = min_of_three(10,-20,30)
print(minimum)



#write a function name Absolute_value and that takes a value and return its absolute value without using build in function 
#without suing abs(nm)
def Absolute_value(num):
    if num>=0:
        return num
    return num *-1

print(Absolute_value(50))
print(Absolute_value(-9))




# Keyword Arguments
#                     Required argument 
def calculate_marks(maths, eng, hindi, comp, history=0):  # history=0 means its Default argument.right side 
    print(f"maths = {maths}")
    print(f"eng = {eng}")
    print(f"hindi = {hindi}")
    print(f"comp = {comp}")
    print(f"history = {history}")
    total_marks = maths + eng + hindi + comp + history
    print(f"Total marks scored = {total_marks}")



calculate_marks(hindi=22, maths=11, history=99, comp=56, eng=87)   # positional arguments or keyword argument






#lambda Functions 
is_adult=lambda age: True if age>=18 else False
print(is_adult(10))




#Question 
# write a function  that called min_of_three and take three numbers and return the smallest without using any build in function 
def min_of_three(num1,num2,num3):
    if num1<num2 and num1<num3:
        return num1
    elif num2<num1 and num2<num3:
        return num2
    return num3
minimum = min_of_three(10,-20,30)
print(minimum)


