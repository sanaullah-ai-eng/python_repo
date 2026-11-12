def calculate(a:int,b:int  ) ->int :  # -> int returning in int or returning something 
    return a +b
# calculate("6"  , 7 )
print(calculate(1,2))

def cal_mazimum(a:int,b:int,c:int) ->None:
    print(f"mazimum of a b c is {max(a,b,c)}")
cal_mazimum(3,5,6)  # not returning somehting we cannot store this 



# anotations examples 
def maxi(nums:list[int])->int:  # writing in annotations 
    return max(nums)
number = [ 11,2,23,555,666]
maximum = maxi(number)
print(maximum)


# Type annotations also knows as type hints 
