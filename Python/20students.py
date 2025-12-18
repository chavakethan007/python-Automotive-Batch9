students={"chava": "kethan",
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
    "verma": "rahul"}

'''for i in range(1,21):
    surname=input("Enter surname: ")
    name=input("Enter name: ")

    students[surname]=name'''

for surname,name in students.items():
    print({surname},{name})

name_count={}

for surname, name in students.items():
    if name in name_count:
        name_count[name].append(surname)
    else:
        name_count[name] = [surname]

for name, surnames in name_count.items():
    if len(surnames) > 1:
        print(name, surnames)

