name=[10,20,40,20,10,50,78,98,88,888]
print(len(name))
print(type(name))
#updating value 
name[-1]=28
print(name)
#Maxi
maxi=max(name)
print(f"Maximun Number {maxi}")
#mini
mini=min(name)
print(f"Minimun Number {mini}")
#Total
total=sum(name)
print(f"Sum Number {total}")
#sorting
new_list=sorted(name)
print(f"Soted Number {new_list}")
# sorted in reverse order 
new_list=sorted(name , reverse=True)
print(f"Soted Number Reverse  {new_list }")

lst=[10,20,40,20,10,50,78,98,88,888]
n = len(lst)
for i in range(0,n):
    print(lst[i], end=" ")
    i+=1




# using Eneumerate we can do things like this . 
for index , value  in enumerate(lst):
    print(f"index = {index} and value {value}" )

    