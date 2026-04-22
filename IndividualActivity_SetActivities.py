# Trying out Sets in Python

# -------------------------------
# Activity 1: Remove Duplicates
# -------------------------------
print("=== Activity 1 ===")

numbers = [1, 2, 2, 3, 4, 4, 5]

# convert list to set to remove duplicates
unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique values:", unique_numbers)


# -------------------------------
# Activity 2: Add and Remove
# -------------------------------
print("\n=== Activity 2 ===")

fruits = {"apple", "banana"}
print("Starting fruits:", fruits)

# add orange
fruits.add("orange")

# remove banana
fruits.remove("banana")

print("Updated fruits:", fruits)


# -------------------------------
# Activity 3: Set Operations
# -------------------------------
print("\n=== Activity 3 ===")

A = {1, 2, 3}
B = {3, 4, 5}

# union (combine both sets)
union_result = A | B

# intersection (common values)
intersection_result = A & B

print("Set A:", A)
print("Set B:", B)
print("Union:", union_result)
print("Intersection:", intersection_result)


# -------------------------------
# Activity 4: Common Students
# -------------------------------
print("\n=== Activity 4 ===")

classA = {"Angelo", "Darren", "Joshua"}
classB = {"Darren", "Joshua", "Jasmine"}

# students in both classes
both_classes = classA & classB

# all students
all_students = classA | classB

print("Students in both classes:", both_classes)
print("All students:", all_students)
