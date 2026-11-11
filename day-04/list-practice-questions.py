# Give two list and merg them into one new list without modifiying the existing once 
lst1=[1,2,3,4]
lst2=[1,2,3,4]

new_list=lst1+lst2
print(new_list)


#using Fuction mergining the lists 
def merg_two_lists(lst1,lst2):
    new_list=[]
    for num in lst1:
        new_list.append(num)
    for num in lst2:
        new_list.append(num)
    return new_list

print(merg_two_lists(lst1,lst2))
        




#Giving a list , REmove all the dublicate element while preserving the orignal order of the uniqe items 
def  removing_dublicate(lst):
    result=[]
    for num in lst:
        if num not in result:
            result.append(num)
    return result 

nums=[1,1,1,1,1,2,22,2,2,2,3,4,5,34,2,2,3,3,]
print(removing_dublicate(nums))



