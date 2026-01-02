from abc import ABC, abstractmethod

# ---------------- ABSTRACTION ----------------
class Person(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass


# ---------------- INHERITANCE + ENCAPSULATION ----------------
class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks   # private variable (Encapsulation)

    def get_role(self):
        return "Student"

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def get_role(self):
        return "Teacher"


# ---------------- MAIN PROGRAM ----------------
students = []

while True:   # WHILE LOOP
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    try:   # EXCEPTION HANDLING
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            s = Student(name, marks)
            students.append(s)
            print("Student added successfully")

        elif choice == 2:
            if not students:
                print("No students available")
            else:
                print("\nStudent Details:")
                for s in students:   # FOR LOOP
                    print("------------------")
                    print("Name:", s.name)
                    print("Role:", s.get_role())   # POLYMORPHISM
                    print("Marks:", s.get_marks())

        elif choice == 3:
            print("Exiting system...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Error: Please enter numeric input only")
