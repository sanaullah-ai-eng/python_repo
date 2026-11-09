"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
"""
for i in range(1,6):
    for j in range(1,6):
        print(j , end= " ")
    print()





"""
1 1 1 1 1 
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5 
"""
print()
print("pattren 2")
for i in range(1,6):
    for j in range(1,6):
        print(i , end=" ")
    print()







"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""
print()
print("pattren 3 ")
for i in range(5,0 ,-1):
    for j in range(1,6):
        print(i , end=" ")
    print()






"""
*
* *
* * *
* * * *
* * * * *
"""
print()
for i in range(1 , 6 ):
    for j in range(1,i+1):
        print("*" , end=" ")
    print()










"""
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""
print()
for i in range(1 , 6 ):
    for j in range(1,i+1):
        print(j , end=" ")
    print()








"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
"""

print()
for i in range (1 , 6 ):
    for j in range( i , 0  , -1):
        print(j,end=" ")
    print()





print()
"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
"""
for i in range(5,0,-1):
    for j in range(1 ,i+1):
        print(j , end=" ")
    print()






"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""

print()
for i in range(5, 0 , -1):
    for j in range(i , 0 , -1):
        print(j , end=" ")
    print()





print()
"""
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
first solve half and then half problem 
"""

for i in range(1 , 6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()





print()
"""
5
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
5 4 3 2
5 4 3 
5 4 
5

"""
for i in range(5 , 0 , -1):
    for j in range(5 , i-1 , -1):
        print(j , end=" ")
    print()
for i in range(1 , 6):
    for j in range(5 , i , -1):
        print(j , end=" ")
    print()





print()
"""
        1
      1 2 
    1 2 3 
  1 2 3 4
1 2 3 4 5 
"""
for i in range(1,6):
    for k in range(i , 6-1):
        print(" " , end=" ")
    for j in range(1 , i +1 ):
        print(j, end=" ")
    print()





print()
