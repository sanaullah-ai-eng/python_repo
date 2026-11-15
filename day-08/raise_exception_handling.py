def check_age(age:int):
    if age<0:
        raise ValueError ("Age cannot be negitive .")
    elif age>=150:
        raise ValueError("Age wrong")
    print("your age is good ")
try:
    check_age(1000)

except ValueError as e:
    print(e)
except Exception as e :
    print(e)
