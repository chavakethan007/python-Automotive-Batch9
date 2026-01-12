class BankAccount:
    def __init__(self, name, account_number, balance):
        # Instance variables
        self.name = name
        self.account_number = account_number
        self.__balance = balance   # Encapsulation (private variable)

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    # Abstraction: user doesn't know internal balance logic
    def show_balance(self):
        print("Current Balance:", self.__balance)

    # Method to display account details
    def show_details(self):
        print("\nAccount Holder:", self.name)
        print("Account Number:", self.account_number)


# Creating objects
acc1 = BankAccount("Ravi", 101, 5000)
acc2 = BankAccount("Anu", 102, 8000)

# Using object methods
acc1.show_details()
acc1.deposit(2000)
acc1.withdraw(1500)
acc1.show_balance()

acc2.show_details()
acc2.withdraw(3000)
acc2.show_balance()
