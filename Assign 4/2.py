'''
list of 12+ numbers from the user, sorts it, 
and extracts specific index ranges using slicing.
'''

try:
    # Take input and convert to list of integers
    user_input = input("Enter at least 12 numbers separated by spaces: ")
    num_list = [int(x) for x in user_input.split()] # Convert input string to list of integers

    if len(num_list) < 12:
        print("Please enter at least 12 elements.")
    else:
        # Sort the list
        num_list.sort()
        print(f"Sorted List: {num_list}")

        # Slicing operations
        print(f"Slice 3-6: {num_list[3:7]}") # 7 stop/exclusive
        print(f"Slice 6-9: {num_list[6:10]}")
        print(f"Slice 4-10: {num_list[4:11]}")
except ValueError:
    print("Invalid input! Please enter numbers only.")