import random

# Generate dice value between 1 and 6
dice = random.randint(1, 6)

# Player guess
guess = int(input("Guess the dice value (1-6): "))

# Check result
if guess == dice:
    print(f"Correct! Dice was {dice} 🙂")  # Smiling face
elif abs(guess - dice) == 1:
    print(f"Close! Dice was {dice} 😐")    # Neutral face
else:
    print(f"Wrong! Dice was {dice} 😞")    # Sad face