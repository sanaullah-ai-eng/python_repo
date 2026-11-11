# Strings are immutable

name = "sanaullah"
print(name, id(name))

# Override
name = "arif"
print(name, id(name))
# name[0] = "Z"
# print(name)










"""
String Methods: Splitting and Joining
split(): Break String into List
join(): Combine List into String
"""

# text = "Sanaullah is a coder"

# print(len(text.split()))

my_list = ["s", "a", "n", "a", "u", "ll", "ah", 5, 55.33, "python", "coder"]
ans = "-".join(str(ch) for ch in my_list)
print(ans)
print(type(ans))








text = "sanaullah is a good coder and is learning python"
# python learning is and coder....sanaullah

words_list = text.split()
words_list = words_list[::-1]
print(" ".join(words_list))








#slicing
text = "Programming"

print(text[0:4])
print(text[4:10])
print(text[:6])
print(text[6:])
print(text[:])
print(text[10:5:-1])
print(text[7::-1])
print(text[::-1])  # Reverse a string
print(text[1:8:2])