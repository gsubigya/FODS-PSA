# Function definitions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def floor_div(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot divide by zero"

def exponent(a, b):
    return a ** b

# Take inputs
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Display results
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")
print(f"{x} // {y} = {floor_div(x, y)}")
print(f"{x} ** {y} = {exponent(x, y)}")