# Input numbers from the user, separated by spaces
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Remove duplicates and sort
unique_sorted = sorted(set(numbers))

# Display result
print("List after removing duplicates and sorting:", unique_sorted)