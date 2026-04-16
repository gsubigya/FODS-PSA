"""
basic numpy operations
operations: sum, mean, maximum, and minimum
"""
import numpy as np

# Create the array
arr = np.array([10, 20, 30, 40, 50])

print(f"Array: {arr}")

# a) Find total sum
print(f"Total Sum: {np.sum(arr)}")

# b) Calculate mean value
print(f"Mean Value: {np.mean(arr)}")

# c) Largest and smallest values
print(f"Largest Value: {np.max(arr)}")
print(f"Smallest Value: {np.min(arr)}")