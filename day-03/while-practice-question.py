#Question no 1 : 
#  print all the number which are divisable by 3 and 5 from 1 to 100
start=1
end=100
i = start 
print("divisable by 3 and 5 from 1 to 100")
while i<=end:
    if i%3==0 and i%5==0:
        print(i , end=" ")
    i+=1




print(' ')
# Question no 02 
# sum of all the numbers 1 to 100
start=1
end=100
j = start 
sum=0
print("Sum of 1 to 100 ")
while j<=end:
    # print(j,end=" ")
    sum+=j    #adding sum 
    j+=1
    
print("sum is : " , sum)





print(" ")
# Question no 03 
# sum of all the numbers 1 to 100 whos divisable by 2 and 7 
start=1
end=100
j = start 
sum=0
print("Sum of 1 to 100  whoes divisable by 2 and 7 ")
while j<=end:
    # print(j,end=" ")
    sum+=j    #adding sum 
    j+=1
    if sum%2==0 and sum%7==0:
        print(sum , end =" ")





print(" ")
# Question no 04 
#print mutliplication table 
user_input=int(input("Enter your number : "))
i = 1 
while i<=10:
    print(f"{user_input} x {i} = {i*user_input}")
    i+=1






print(" ")
# Question no 05
# Ask a number from a user and print the factorial of the number 
user=int(input("Enter your Number : "))
i = 1
print(f"{user} all factorial : ")
while i<=user:
    if user%i==0:
        print(i ,end=" ")
    i+=1


