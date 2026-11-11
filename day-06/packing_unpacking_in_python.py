# take a function which retrun min and max value of the list 

def min_max(lst):
    maxi=max(lst)
    mini=min(lst)
    return min,max # here is we doing the unpacking

# random_lst=[1,4,7,8,5,6,8,8,85,3,4,5,6]
print(min_max([1,4,7,8,5,6,8,8,85,3,4,5,6]))


# Packing: grouping multiple values into a single tuple
person = "Alice", 28, "Engineer"

# Unpacking: extracting tuple values into separate variables
name, age, job = person

print(name)  # Output: Alice
print(age)   # Output: 28
print(job)   # Output: Engineer











numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)   # Output: 10
print(middle)  # Output: [20, 30, 40]
print(last)    # Output: 50








def summarize_order(*items, **details):
    print("Items ordered:", items)       # Packed into a tuple
    print("Order details:", details)     # Packed into a dictionary

summarize_order("Laptop", "Mouse", customer="Bob", express=True)
# Output:
# Items ordered: ('Laptop', 'Mouse')
# Order details: {'customer': 'Bob', 'express': True}
