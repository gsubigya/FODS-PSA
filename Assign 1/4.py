import math

# user input
num = float(input("Enter a number: "))

# Perform calculations
cube = num ** 3
cube_root = num ** (1/3)
natural_log = math.log(num)
base_2 = math.log2(num)
power_6 = num ** 6

# Display results
print(f"Cube of {num}^3 = {cube}")
print(f"Cube Root og {num} = {cube_root}")
print(f"Natural Log (ln): ln({num}) = {natural_log}")
print(f"Log base 2: log2({num}) = {base_2}")
print(f"Power 6: {num}^6 = {power_6}")