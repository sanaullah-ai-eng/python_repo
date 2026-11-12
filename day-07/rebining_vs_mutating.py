# Rebining and mutating 
def rebing(x):
    x=[100,200,300]
    print(id(x))    # id diffrent but know x inside the function is also variable another variable 
    print(f"inside the function = {x}")
    
nums=[1,2,3]
rebing(nums) 
print(f"Outside the function = {nums}")
print(id(nums))  





# mtating
def mutate(x):
    x[0]=100
    print(id(x))    
    print(f"inside the function = {x}")
    
nums=[1,2,3]
mutate(nums) 
print(f"Outside the function = {nums}")
print(id(nums))  

# here is mutating 


