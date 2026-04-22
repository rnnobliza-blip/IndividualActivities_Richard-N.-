# Exploring Dictionaries in Python

# -------------------------------
# Activity 1: Fill in the Blanks
# -------------------------------
student = {
    "name": "Richard",
    "age": 19,
    "course": "BSIT"
}

# I think this should print the name
print("Student name:", student["name"])


# -------------------------------
# Activity 2: Add and Update
# -------------------------------
print("\n--- Updating student info ---")

student = {"name": "Richard", "age": 19}

# adding a new key
student["grade"] = 90

# updating age
student["age"] = 20

print("Updated student:", student)


# -------------------------------
# Activity 3: Loop Through Dictionary
# -------------------------------
print("\n--- Car Info ---")

car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

# printing keys and values
for key, value in car.items():
    print(key, ":", value)


# -------------------------------
# Activity 4: Mini Phonebook
# -------------------------------
print("\n--- Mini Phonebook ---")

phonebook = {
    "Richard": "09637280354",
    "Ate Sarah": "09621584253",
    "Jhon Bhrix": "09551234567"
}

# ask user for a name
name = input("Enter a name to search: ")

# check if name exists
if name in phonebook:
    print("Phone number:", phonebook[name])
else:
    print("Sorry, name not found.")
