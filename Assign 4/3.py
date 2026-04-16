'''
generates a 1x12 array of random integers, 
sorts it, and reshapes it into a 3x4 matrix.
'''
import numpy as np

# Generate 12 random integers between 1 and 100
random_arr = np.random.randint(1, 101, size=12) # 1x12 array of random integers
print(f"Original Array: {random_arr}")

# Sort the array
sorted_arr = np.sort(random_arr)
print(f"Sorted Array: {sorted_arr}")

# Reshape to 3x4 matrix
matrix_3x4 = sorted_arr.reshape(3, 4)
print("\nFinal Reshaped 3x4 Matrix:")
print(matrix_3x4)