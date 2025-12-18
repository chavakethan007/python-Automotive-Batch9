# Creating a dictionary
student = {
    "name": "Kethan",
    "age": 21,
    "branch": "CSE",
    "cgpa": 8.93
}

# Accessing values
print(student["name"])          # Access using key
print(student.get("age"))       # Safe access

# Modifying value
student["age"] = 22

# Adding new key-value
student["college"] = "ABC Engineering"

# Removing elements
student.pop("branch")           # Remove by key
removed_item = student.popitem()# Removes last inserted item

# Dictionary views
print(student.keys())           # All keys
print(student.values())         # All values
print(student.items())          # Key-value pairs

# Copy dictionary
student_copy = student.copy()
print(student_copy)

# Update dictionary
student.update({"cgpa": 9.0, "city": "Hyderabad"})

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# Clear dictionary
student.clear()
print(student)
