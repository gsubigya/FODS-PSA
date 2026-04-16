'''
creates a staff class, takes multiple staff inputs, 
saves them to 'staff.csv', and allowing the user to view the file contents.
'''
import csv

class Staff:
    def __init__(self, emp_id, name, address, phone, status, dependents, salary):
        self.emp_id = emp_id
        self.name = name
        self.address = address
        self.phone = phone
        self.status = status
        self.dependents = dependents
        self.salary = salary

def save_staff_to_file(staff_list):
    try:
        with open("staff.csv", "a", newline='') as file:
            writer = csv.writer(file)
            for s in staff_list:
                writer.writerow([s.emp_id, s.name, s.address, s.phone, s.status, s.dependents, s.salary])
        print("\nSuccess! Data saved to staff.csv.")
    except Exception as e:
        print(f"Oops! Error occurred while saving: {e}")

def view_staff():
    try:
        print("\n--- Existing Staff List ---")
        with open("staff.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}, Phone: {row[3]}, Marital Status: {row[4]}, Dependents: {row[5]}, Salary: {row[6]}")
    except FileNotFoundError:
        print("Error! The file 'staff.csv' does not exist.")

# Main Menu
staff_members = []
while True:
    choice = input("\n1. Add Staff \n 2. View All Staff \n 3. Exit \n Enter choice: ")
    if choice == '1':
        try:
            ids = input("ID: ")
            name = input("Full Name: ")
            addresss = input("Address: ")
            phone = input("Phone: ")
            mstatus = input("Married? (Single/Married): ")
            dependent = input("Dependents: ")
            salary = input("Salary: ")
            
            staff_members.append(Staff(ids, name, addresss, phone, mstatus, dependent, salary))
            save_staff_to_file(staff_members)

            staff_members.clear() # Clearing list after saving to avoid duplicates
        except Exception as e:
            print(f"Input error: {e}")
    elif choice == '2':
        view_staff()
    elif choice == '3':
        break