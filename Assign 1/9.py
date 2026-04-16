positive_sum = 0
negative_sum = 0

while True:
    print("\n1. Enter number  2. Show sums  3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        num = float(input("Enter a number: "))
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num
        else:
            print("Zero is ignored.")

    elif choice == "2":
        print("Sum of positives:", positive_sum)
        print("Sum of negatives:", negative_sum)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")