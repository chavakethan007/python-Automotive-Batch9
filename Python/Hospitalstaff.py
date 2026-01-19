# Base class
class Hospital_staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_duties(self):
        print("Staff duty")

    def calculate_salary(self):
        print(f"Salary: {self.salary}")


# Doctor class
class Doctor(Hospital_staff):
    def __init__(self, name, salary, consultation_fee):
        super().__init__(name, salary)
        self.consultation_fee = consultation_fee

    def get_duties(self):
        print(f"Dr. {self.name} treats patients")

    def calculate_salary(self):
        total = self.salary + self.consultation_fee
        print(f"Doctor Salary: {total}")


# Nurse class
class Nurse(Hospital_staff):
    def __init__(self, name, salary, extra_bonus):
        super().__init__(name, salary)
        self.extra_bonus = extra_bonus

    def get_duties(self):
        print(f"Nurse {self.name} takes care of patients")

    def calculate_salary(self):
        total = self.salary + self.extra_bonus
        print(f"Nurse Salary: {total}")


# Receptionist class
class Receptionist(Hospital_staff):
    def __init__(self, name, salary, festival_bonus):
        super().__init__(name, salary)
        self.festival_bonus = festival_bonus

    def get_duties(self):
        print(f"Receptionist {self.name} manages appointments")

    def calculate_salary(self):
        total = self.salary + self.festival_bonus
        print(f"Receptionist Salary: {total}")

# -------- User Input --------
staff_list = []

n = int(input("Enter number of staff members: "))

for i in range(n):
    print("\n1.Doctor\n2.Nurse\n3 Receptionist")
    choice = int(input("Choose staff type: "))

    name = input("Enter name: ")
    salary = int(input("Enter base salary: "))

    if choice == 1:
        fee = int(input("Enter consultation fee: "))
        staff_list.append(Doctor(name, salary, fee))

    elif choice == 2:
        bonus = int(input("Enter extra bonus: "))
        staff_list.append(Nurse(name, salary, bonus))

    elif choice == 3:
        festival_bonus = int(input("Enter festival bonus: "))
        staff_list.append(Receptionist(name, salary, festival_bonus))

    else:
        print("Invalid choice")

print("\n--- Staff Details ---")
for staff in staff_list:
    staff.get_duties()
    staff.calculate_salary()
    print()
