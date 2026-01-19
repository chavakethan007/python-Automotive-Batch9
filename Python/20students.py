# Dictionary to store students
# Key   -> Surname
# Value -> First name
students = {
    "chava": "kethan",
    "bathi": "pardhiv",
    "chevi": "pradeep",
    "gunupudi": "chetan",
    "illo": "john",
    "chinthamalla": "prabhas",
    "knoeru": "prasad",
    "ghathamaneni": "mahesh",
    "nandamuri": "taraka rama rao",
    "dagubathi": "rana",
    "kasi": "hari",
    "medi": "nikhil",
    "konidella": "pawan kalyan",
    "narendra": "modi",
    "kalvakuntla": "chandrasekhar rao",
    "nara": "chandra babu",
    "reddy": "suresh",
    "naidu": "suresh",
    "sharma": "rahul",
    "verma": "rahul"
}


# Optional code to take input from user
# (Currently commented because data is already given)
'''
for i in range(1, 21):
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    students[surname] = name
'''
# Print all students (surname and name)
for surname, name in students.items():
    print({surname}, {name})

# Dictionary to count names
# Key   -> First name
# Value -> List of surnames having that name
name_count = {}

# Group surnames by same first name
for surname, name in students.items():
    if name in name_count:
        name_count[name].append(surname)
    else:
        name_count[name] = [surname]

# -------------------------------
# Print only duplicate names
# (same first name with different surnames)
# -------------------------------
for name, surnames in name_count.items():
    if len(surnames) > 1:
        print(name, surnames)
