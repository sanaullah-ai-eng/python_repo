
new_dict={'sana': 20,
           'fatima': 50,
            'me': 40, 
            'sanaullah': 1111,
            'gender': 'male'}


# printing the keys and values using the loop 

print(new_dict)

for sub in new_dict.keys():
    print(sub , new_dict[sub])







students = {
    "student_1": {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science"
    },
    "student_2": {
        "name": "Bob",
        "age": 22,
        "major": "Mathematics"
    }
}
print(students["student_1"]["name"])  # Output: Alice
students["student_1"]["age"] = 21               # Updates age
students["student_2"]["grade"] = "A"            # Adds a new key-value pair
