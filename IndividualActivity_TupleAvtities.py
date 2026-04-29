# My Tuple Activities in Python
# Tuple = ordered, indexed, and cannot be changed

print("Learning Tuples in Python")
print("-------------------------")

# Activity 1: Accessing tuple elements
print("\nActivity 1: Access Elements")

favorite_colors = ("red", "green", "blue")

print("First color is:", favorite_colors[0])
print("Last color is:", favorite_colors[-1])


# Activity 2: Tuple slicing
print("\nActivity 2: Slicing")

numbers = (10, 20, 30, 40, 50)

# display 20, 30, 40 only
middle_numbers = numbers[1:4]
print("Middle numbers:", middle_numbers)


# Activity 3: Tuple methods
print("\nActivity 3: Tuple Methods")

my_numbers = (1, 2, 2, 3, 2)

# checking how many times 2 appears
total_twos = my_numbers.count(2)

# finding where number 3 is located
position_of_three = my_numbers.index(3)

print("Number 2 appears:", total_twos, "times")
print("Number 3 is found at index:", position_of_three)


# Activity 4: Packing and unpacking
print("\nActivity 4: Packing and Unpacking")

coordinates = (5, 10)

x, y = coordinates

print("Value of x:", x)
print("Value of y:", y)


# Activity 5: Combining tuples
print("\nActivity 5: Combine Tuples")

first_tuple = (1, 2)
second_tuple = (3, 4)

combined_tuple = first_tuple + second_tuple
repeated_tuple = combined_tuple * 2

print("Final output:", repeated_tuple)
