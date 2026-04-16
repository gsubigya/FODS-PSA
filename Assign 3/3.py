'''
Program to do arithmetic operations
by storing the output with date and time and display on exit 
'''

from datetime import datetime

filename = "Calculation_Rec.txt"

while True:
    num = list(map(int, input("Enter Numbers like (3,4,8,4,5,7) separeted by comma: ").split(",")))
    #numbers = numbers.split(",")

    length = len(num)

    if length < 2:
        print("Please enter at least two numbers.")
        continue

    #a,b = numbers[0], numbers[1] this only prints 2number

    #operations
    adding = sum(num)

    subtracting = num[0]
    for i in range(1, length):
        subtracting -= num[i]

    multiplying = 1
    for i in num:
        multiplying *= i

    dividing = num[0]
    try:
        for i in range(1, length):
            dividing /= num[i]
    except ZeroDivisionError:
        dividing = "Undefined (division by zero)"

    #saving to file
    with open(filename, 'a') as file:
        file.write(f"\n{datetime.now()} \n Numbers: {num} \n Addition: {adding} \n Subtraction: {subtracting} \n Multiplication: {multiplying} \n Division: {dividing:.6f}\n")

    choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if choice != 'yes':
        print("Exiting the program. Calculation history saved in Calculation_Rec.txt")
        break

#Displaying file contents on exit
print("\nCalculated Operations:")
with open(filename, 'r') as file:
    print(file.read())