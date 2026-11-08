# 1 to 10 print 
i = 1
while i<=10:
    print(i , end=' ')
    i+=1
print("")
# 1 to n print 
j= 1 
n = int(input("Enter n value : "))
while j<=n:
    print(j,end=" ")
    j+=1
print(" ")




# Take input start and end and print in loop 
start=int(input("Enter Start Value :"))
end = int(input('Enter End value : '))
#dont change input 
k=start
while k<=end:
    print(k , end=' ')
    k+=1
print(" ")
print("start value is ",start)




#start to end even numbers 
start=int(input("Enter Start Value :"))
end = int(input('Enter End value : ')) 
l = start 

while l<=end :
    if l%2==0:
        print(l,end=' ')
    l+=1
print(" ")



#print the number whoes are divisibleby 3 and 4 
start=int(input("Enter Start Value :"))
end = int(input('Enter End value : ')) 
m = start
while m<=end:
    if m%3==0 and m%4==0:
        print(m , end=' ')
    m+=1
print(' ')






# 10 to 1 
o=10
print("reverse number : ")
while o>=1:
    print( o ,end=" ")
    o-=1