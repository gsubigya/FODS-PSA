'''
Program to copy content from one file to another using try/except handling.
'''

import os

input_file = input("Enter input file name: ")
output_file = input("Enter output file name: ")

try:
    # Check if input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file does not exist.")

    # Check if output file already exists
    if os.path.exists(output_file):
        raise FileExistsError("Output file already exists.")

    with open(input_file, "r") as input_files:
        content = input_files.read()
    with open(output_file, "w") as output_files:
        output_files.write(content)


    print("File copied successfully!")

except FileNotFoundError as e:
    print("Error:", e)

except FileExistsError as e:
    print("Error:", e)