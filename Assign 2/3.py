# Function to check Armstrong number
def is_armstrong(num_str):
    if not num_str.isdigit():
        return "Invalid input! Not a number."
    
    num = int(num_str)
    digits = [int(d) for d in num_str]
    power = len(digits)
    total = sum(d ** power for d in digits)
    
    if total == num:
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is NOT an Armstrong number."

# Input from user
s = input("Enter a number: ")
print(is_armstrong(s))