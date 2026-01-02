# This function is a decorator factory
# It takes 'n' as input to decide which operation to perform
def calculator(n):

    # This is the actual decorator
    # It receives the function (add, subtract, etc.)
    def decorator(func):

        # This function replaces the original function
        # It takes two numbers a and b
        def assign(a, b):

            # If choice is 1 → Addition
            if n == 1:
                return a + b

            # If choice is 2 → Subtraction
            elif n == 2:
                return a - b

            # If choice is 3 → Multiplication
            elif n == 3:
                return a * b

            # If choice is 4 → Division
            elif n == 4:
                # Handling division by zero error
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return a / b

            # If invalid choice
            else:
                return "Invalid choice"

        # Return the modified function
        return assign

    # Return the decorator
    return decorator


# Decorator applied with n = 1 (Addition)
@calculator(1)
def add(a, b):
    pass   # Function body not needed because decorator handles logic


# Decorator applied with n = 2 (Subtraction)
@calculator(2)
def subtract(a, b):
    pass


# Decorator applied with n = 3 (Multiplication)
@calculator(3)
def multiplication(a, b):
    pass


# Decorator applied with n = 4 (Division)
@calculator(4)
def division(a, b):
    pass


# Taking user input for choice
n = int(input("Enter Choice: 1)add 2)subtract 3)Multiplication 4)Division: "))

# Taking input numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calling the corresponding decorated function
if n == 1:
    print("Result: ", add(a, b))
elif n == 2:
    print("Result: ", subtract(a, b))
elif n == 3:
    print("Result: ", multiplication(a, b))
elif n == 4:
    print("Result: ", division(a, b))
else:
    print("Invalid choice")

