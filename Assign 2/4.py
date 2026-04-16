# Function to count occurrences
def count_occurrences(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

# Test the function with three lists
list1 = [1, 2, 2, 3, 1, 4, 2, 3, 4, 4]
list2 = [5, 5, 5, 6, 7, 6]
list3 = [8, 9, 8, 10, 10, 10]

print("List 1 counts:", count_occurrences(list1))
print("List 2 counts:", count_occurrences(list2))
print("List 3 counts:", count_occurrences(list3))