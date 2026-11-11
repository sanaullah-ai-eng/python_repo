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






# take a 3x3 matric and then use the nested loop to calclate and print all elemnt 
# total_element=[
#     [1,2,3],
#     [2,3,4],
#     [4 ,5,6]
# ]

# rows=len(total_element)
# coloum=len(total_element[0])
# for i in range(0,rows):
#     for j in range(0,coloum):
#         print(total_element[i][j] ,end=" ")
#     print() 









#write aprograme which take input from the user and  store the number in 
# list and seperate the even and seperate the odd and print 
# them in seperate order or store them in seperate list 
# after doing this take those lists and store them into one list 


# while True:
#     user_input=int(input("Enter Your list data : "))
#     lst = lst[user_input]







#Give a 3x3 matrix as input and prints its lower triangle replace element in upper triangle 
#with in astaric.

#upper part ko mean upper triangle ko bnana kaliya likss this 
"""
1 * * 
4 5 * 
7 8 9 

"""

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

r=len(matrix)
c=len(matrix)

for i in range(0,r):
    for j in range(0,c):
        if i>=j:
            print(matrix[i][j] , end=' ')
        else:
            print('*' , end=" ")
    print()




print()

"""
1  *  * 
*  2  * 
*  *  3 
print this 


"""

matrice=[
    [1,2,3],[4 , 2,6 ] , [7,8,3]
]
coloum=len(matrice)
rowss=len(matrice)

for i in range(0,rowss):
    for j in range(0,coloum):
        if i==j:
            print(matrice[i][j],end=" ")
        else:
            print("*" , end=" ")
    print()





"""
*  *  3 
*  2  * 
7  *  * 
print this 
 adding i and j its all the common words so we add those and == rows-1

"""
print()
matrice=[
    [1,2,3],[4 , 2,6 ] , [7,8,3]
]
coloum=len(matrice)
rowss=len(matrice)

for i in range(0,rowss):
    for j in range(0,coloum):
        if i+j==rowss-1:
            print(matrice[i][j],end=" ")
        else:
            print("*" , end=" ")
    print()