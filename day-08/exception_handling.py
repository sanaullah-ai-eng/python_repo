try:
    num = int(input("Enter your number : "))
    result = 100/num
except ValueError:
    print("Enter a valid value please. ")
except TypeError:
    print("Enter the correct type value. ")
except ZeroDivisionError:
    print("Enter the valid number not Zero .")
else:
    print(f"Result : {result}")
finally :
    print("Code compeleted Run finally.")