import random

# Game Rules
print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

choices = ["Rock", "Paper", "Scissors"]

while True:

    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    #Validate user input
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    while choice < 1 or choice > 3:
        choice = int(input("Please enter a valid choice (1-3): "))

    #User choice
    user_choice = choice[choices - 1]

    print("\nUser choice is:", user_choice)
    print("Now it's Computer's Turn...")