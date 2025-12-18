# -----------------------------------
# Python I/O Expressions Example
# -----------------------------------

# Taking string input from the user
name = input("Enter your name: ")

# Taking integer input and converting it to int
age = int(input("Enter your age: "))

# Taking float input and converting it to float
height = float(input("Enter your height: "))

# Taking boolean input
# input() returns a string, so we compare it with "True"
passed = input("Passed (True/False): ") == "True"

# Displaying output using print() function
print("User Details")

# Printing values using comma (automatic spacing)
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Passed:", passed)

# Printing output using string formatting (f-string)
print(f"My name is {name}, I am {age} years old and my height is {height}")
