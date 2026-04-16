'''
Program to create a Learner class and display details.
roll_no, full_name, address, enrollment_year, program, and group
'''

class Learner:
    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    def display(self):
        print("\n--- Learner Details ---")
        print("Roll No:", self.roll_no)
        print("Name:", self.full_name)
        print("Address:", self.address)
        print("Enrollment Year:", self.enrollment_year)
        print("Program:", self.program)
        print("Group:", self.group)


# Taking input
learner = Learner(
    input("Roll No: "),
    input("Full Name: "),
    input("Address: "),
    input("Enrollment Year: "),
    input("Program: "),
    input("Group: ")
)

learner.display()