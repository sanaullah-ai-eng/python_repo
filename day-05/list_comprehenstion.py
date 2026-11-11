# Normal way 
square=[1,2,3,4,5]
for i in range(1, 6 ):
    square.append(i*i)
print(square)


# square2=[2,4,7 ,9]
square2=[i*i for i in range(1,6)]
print(square2)


# print the even number using the list comprehenstion 

new_list=[i for i in range(1,11) if i%2==0]
print(new_list)


print()
print("Prime number print")
# from 1 to 100 make a list of prime numbers 
def is_prime(num):
    factor=0
    for i in range(1,num+1):
        if num%i==0:
            factor+=1
    if factor==2:
        return True 
    return False

prime_list=[i for i in range(2,101) if is_prime(i)==True]
print(prime_list)




print()
print("Odd Numbers print")
# using list comprehenstion create a list of square of odd numbers 
new_list_odd_numbers =[i*i for i in range(1 , 21)  if i %2==1]
print(new_list_odd_numbers)