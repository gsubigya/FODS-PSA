#user input
user_input = input("Enter a positive integer: ")

# Validate input
if not user_input.isdigit():
    print("Invalid input! Please enter a positive integer.")
else:
    num = int(user_input)
    
    # Calculate factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    
    # Display result
    print(f"Factorial of {num} is {factorial}")