# write a python script that iterate through a list of integer and 
# replace every nagitive number found in the list with 0 

def replace_nagitive(lst):
    n = len(lst)
    result=[]
    for i in range(0,n):
        if lst[i]<0:
            lst[i]=0
    return lst

nums=[1,1,1,-2,2,3,-4,6,8,-5]
print(replace_nagitive(nums))








#write aprograme which take input from the user and  store the number in 
# list and seperate the even and seperate the odd and print 
# them in seperate order or store them in seperate list 
# after doing this take those lists and store them into one list 


while True:
    user_input=int(input("Enter Your list data : "))
    lst = lst[user_input]


