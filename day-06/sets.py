my_set = {5, 5, 2, 4, 5, 5, 6, 5, "Anirudh", "Khurana", 99.99, 5}
print(my_set)
print(type(my_set))

# How to create an empty set
sett = set()
print(sett)
print(type(sett))





#type converstion 
# Type Conversion
my_set = {5, 5, 2, 4, 5, 5, 6, 5, "Anirudh", "Khurana", 99.99, 5}
print(list(my_set))


my_list = [54, 65, 43, 32, 32, 3, 43, 43, 43, 43]
print(list(set(my_list)))


# adding element 
# Use add() for single elements, and
# update() for multiple elements from an iterable.

pythonfruits = {"apple", "mango"}

# pythonfruits.add("kiwi")
# pythonfruits.add("grape")
# pythonfruits.add("lichi")
pythonfruits.update(["kiwi", "grape", "lichi"])
print(pythonfruits)




# removing elements 
# Python offers methods like
# remove(), discard(), pop(), and clear() to manage set elements.
pythonfruits = {"apple", "mango", "banana", "kiwi"}

# pythonfruits.remove("applee")
# pythonfruits.discard("appleee")
# pythonfruits.clear()
removed = pythonfruits.pop()
print(f"removed element = {removed}")
print(pythonfruits)