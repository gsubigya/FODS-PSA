import random

# Computer picks a number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0

print("Guess the number between 1 and 50. You have 7 tries!")

while attempts < 7:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congrats! You guessed it in {attempts} tries.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Better luck next time! The number was {secret_number}.")