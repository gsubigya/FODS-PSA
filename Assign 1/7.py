start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

numbers = []

for num in range(start, end + 1):
    if num % 9 == 0 and num % 6 != 0:
        numbers.append(num)

print("\nNumbers divisible by 9 but not by 6:")
print(numbers)
print(f"Count: {len(numbers)}")