orignal =[1,2,3]
copy=orignal
copy.append(1000)

print(id(copy))   #1282620044736
print(id(orignal))  # 1282620044736 same address and when we change data in copy it also copy in the orignal 



print()

#   Shallow copy using 
# 1st way to do this 
orignals = [1,2,3]
copys =orignals.copy()
copys.append(10000)
print(copy)
print(orignals)
print(id(orignals))   # 2860600717184
print(id(copys))   #2860603104320 diffrent address know its shallow copy 


print()
# other way to doing the shallow copy 
import copy 
lst=[1,3,4]
shallow=copy.copy(lst)
print(id(lst))
print(id(shallow))

shallow.append(10000000000000000)
print(lst)
print(shallow)








#Deep copy 
import copy 
lst=[1,3,4 , [1, 4, 5, 8 ], 8 , 5 , 23]

shallow=copy.deepcopy(lst)
shallow[3][1] = 9999 
print(id(lst))
print(id(shallow))
print(lst)
print(shallow)
 