'''
performs matrix addition, subtraction, and multiplication.
Includes try/except blocks to handle dimension mismatches.
'''
import numpy as np

def matrix_operations():
    try:
        # Define two sample matrices (you can also take these as input)
        # Change dimensions here to test the exception handling
        mat1 = np.array([[1, 2], [3, 4]]) #2x2 matrix
        mat2 = np.array([[5, 6], [7, 8]]) #   "
        print("Matrix 1:\n", mat1)
        print("\nMatrix 2:\n", mat2)

        # Addition & Subtraction (Must be identical dimensions)
        if mat1.shape == mat2.shape:
            print("\nAddition:\n", np.add(mat1, mat2))
            print("\nSubtraction:\n", np.subtract(mat1, mat2))
        else:
            raise ValueError("Matrices must have the same dimensions for +/-.")

        # Multiplication (Standard Dot Product)
        # Note: mat1 columns must match mat2 rows
        dot_product = np.dot(mat1, mat2)
        print("\nDot Product (Multiplication):\n", dot_product)

    except ValueError as e:
        print(f"Dimension Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

matrix_operations()