import ci

class BankAccount:

    def __init__(self, name, age, principal, rate, time):
        self.name = name
        self.age = age
        self.balance = principal
        self.rate = rate
        self.time = time

    def show_details(self):
        return f"Name: {self.name}, Age: {self.age}, Balance: {self.balance}"

    def show_balance(self):
        return f"Current Balance of {self.name}: {self.balance}"

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Invalid withdrawal amount")

            if amount > self.balance:
                return "Error: Insufficient balance"

            self.balance -= amount
            return f"{amount} withdrawn successfully. Remaining balance: {self.balance}"

        except ValueError as e:
            return str(e)
        except Exception:
            return "Unexpected error during withdrawal"

    def calculate_interest(self):
        try:
            # Senior Citizen → Compound Interest
            if self.age > 60:
                amount = ci.compoundinterest(self.balance, self.rate, self.time)
                return f"CI for Senior Citizen {self.name}: {amount}"
            
        except TypeError:
            return "Error: Invalid data type used"
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception:
            return "Unexpected error occurred"
        
acc1 = BankAccount("Ramesh", 65, 10000, 8, 5)
acc2 = BankAccount("Suresh", 45, 15000, 7, 3)
acc3 = BankAccount("Anita", 70, 20000, 6, 4)

print(acc1.show_details())
print(acc1.show_balance())
print(acc1.calculate_interest())

