#Step 1: Generate a random number
import random
number_to_guess = random.randint(1, 60)
attempts = 0
max_attempts = 5

#Step2: Prompt the User
print("♠ welcome to the number guessing game!")
print(" I'm thinking of a number between 1 and 60.")
print(" Can you guess it within 5 attempts? Let's go!\n")

while attempts < max_attempts:
    guess = int(input( "Guess the number: "))
    attempts += 1

    if guess < number_to_guess:
        print(" Too low ! Try again.\n")
    elif guess > number_to_guess:
        print("Too high ! Try again.\n")
    else:
        print(f" Congratulations! You guessed it in { attempts} attempts.")
        break
else:
       print(f" Game Over! The number was {number_to_guess}.Better luck next time! ")

