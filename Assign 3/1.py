'''
Program to read records.csv and show the contents
student_name, roll_no, program, year, and group
'''

import csv

#opening and reading the csv file
try:
    with open('records.csv','r') as file:
        read = csv.reader(file)

        print("\n")
        print("Student Records ::")

        for row in read:
            print(f"Name: {row[0]}, Roll No: {row[1]}, Program: {row[2]}, Year: {row[3]}, Group: {row[4]}")

except FileNotFoundError:
    print("Error! records.csv not found.")