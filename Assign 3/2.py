'''
program to append data to records.csv
'''

import csv

#taking input from user
student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
program = input("Enter program: ")
year = input("Enter year: ")
group = input("Enter group: ")

#appending data to the csv file
try:
    with open('records.csv','a',newline='') as file:
        write = csv.writer(file)
        write.writerow([student_name, roll_no, program, year, group])
        print("Record added successfully!")

except FileNotFoundError:
    print("Try creating records.csv file first!")