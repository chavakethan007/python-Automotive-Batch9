def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y==0:
        print("Error!")
    else:
        return x/y

def calculator():
    x=int(input("Enter 1st number: "))
    y=int(input("Enter 2nd number: "))
    choice=int(input("Enter your choice: 1,2,3,4: "))
    if choice==1:
        print(add(x,y))
    elif choice==2:
        print(subtract(x,y))
    elif choice==3:
        print(multiplication(x,y))
    else:
        print(division(x,y))

calculator()