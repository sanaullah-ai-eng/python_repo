"""
Question No : 01 
write a function fuzzbuzz(n) that take a single number and print Fizz
if it divide by 3
 BuZZ if its divisable by 5 
 fizzbuzz if it divisable by both 
 otherwiser print the number itself .
"""


def fizzbuzz(num):
    if num%3 ==0 and num%5==0:
            return ('fizzbuzz')
    elif num%3==0:
        return ("Fizz")
    elif num%5==0:
        return ("buzz")
    
    return num

print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(20))




"""write a function power base ,exp that 
returns base raised to exp using a loop
 no** operator or poer alllowed """

def power(base, exp):
    if exp == 0:
        return 1
    
    
    is_negative = False
    if exp < 0:
        is_negative = True
        exp = -exp
        
    result = 1
    
    for _ in range(exp):
        result *= base
        
    # If the original exponent was negative, return its reciprocal
    if is_negative:
        return 1 / result
        
    return result


print(power(2, 3))   # Output: 8 (2 * 2 * 2)
print(power(5, 0))   # Output: 1
print(power(2, -2))  # Output: 0.25 (1 / (2 * 2))
