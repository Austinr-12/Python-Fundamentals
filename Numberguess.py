import random

print("Hello!, Welcome to the Number Guessing Game. \n You have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the upper Bound"))

print(f"\nYou have 7 chances to guess the number between {low} and {high}")

num = random.randint(low, high)

# Total allowed chances
ch = 7

# Guess Counter
gc = 0

while gc < ch:
    gc += 1 
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num} You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! that number was {num} Better luck next time.')

    elif guess > num:
        print('Too High! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')

        