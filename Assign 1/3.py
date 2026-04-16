# user input
num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is Positive Even")
    else:
        print("The number is Positive Odd")

elif num < 0:
    if num % 2 == 0:
        print("The number is Negative Even")
    else:
        print("The number is Negative Odd")

else:
    print("The number is Zero")