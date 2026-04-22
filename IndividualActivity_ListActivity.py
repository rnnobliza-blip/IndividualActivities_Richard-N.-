# Playing around with lists in Python

# Start with some fruits
fruits = ["apple", "banana", "cherry"]
print("Original fruits:", fruits)

# Accessing items
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Length of another list
colors = ["red", "blue", "green", "yellow"]
print("Number of colors:", len(colors))


# Modifying the fruits list
print("\n--- Modifying fruits ---")
fruits[1] = "orange"  # I felt like changing banana 😄
print("After change:", fruits)

# Adding items
fruits.append("mango")
fruits.insert(1, "grape")
print("After adding items:", fruits)

# Removing items
fruits.remove("apple")
fruits.pop()  # removes last item
print("After removing items:", fruits)


# Looping through lists
print("\n--- Animals ---")
animals = ["dog", "cat", "bird"]
for animal in animals:
    print("I like", animal)

print("\n--- Numbers with index ---")
numbers = [10, 20, 30]
for i, num in enumerate(numbers):
    print(f"Index {i} has value {num}")


# List operations
print("\n--- Checking items ---")
if "banana" in fruits:
    print("Banana is still here")
else:
    print("Banana is gone 😅")

# Sorting numbers
nums = [5, 2, 9, 1]
nums.sort()
print("Sorted ascending:", nums)

nums.sort(reverse=True)
print("Sorted descending:", nums)

# Copying list
letters = ["a", "b", "c"]
copy_letters = letters.copy()
print("Copied list:", copy_letters)
