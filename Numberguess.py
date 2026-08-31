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