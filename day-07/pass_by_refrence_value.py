# pass by value 
def add_number(x):
    x+=1
    print(id(x))    #140721095278840
    print(f"inside the function = {x}")
    
nums=100
add_number(nums) # number pass by valuue not refrence 
print(f"Outside the function = {nums}")
print(id(nums))  #140721095278808 different ids 




# pass by refrence 
def add_number(x):
    x.append(50)
    print(id(x))    #1968505468352
    print(f"inside the function = {x}")
    
nums=[1,2,3]
add_number(nums) # pass by refrence mutable things pass by refrence 
print(f"Outside the function = {nums}")
print(id(nums))  #1968505468352 same id's 



