# Function to perform operations
def calculate(a, b):
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    
    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Quotient: Division by zero is not allowed!")

# Input two integers from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Call the function
calculate(num1, num2)