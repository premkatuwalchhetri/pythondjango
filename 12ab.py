import random

random_number = random.randrange(1, 5)  # Generate a random number between 1 and 4
attempts = 0
guessed = False

print("Welcome to the game")

while attempts < 5:  # Allow up to 5 attempts
    try:
        guess = int(input("Enter your guessing number: "))
        attempts += 1
        
        if guess == random_number:
            guessed = True
            break  # Exit the loop if the guess is correct
        else:
            print("Try again.")
    except ValueError:
        print("Please enter a valid integer.")

if guessed:
    print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
else:
    print(f"Sorry, you've used all your attempts. The correct number was {random_number}.")
