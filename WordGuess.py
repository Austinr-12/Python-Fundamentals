import random

name = input("What is your name? ")
print("Good Luck!", name)

words = ['rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("\n Guess the characters")

guesses = ''

turns = 12

#beginning main loop for game
while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_", end = " ")
            failed += 1

    print()


    #check if word has been guessed
    if failed == 0:
        print("You Win")
        print("The word is:", word)
        break

    #get the guess
    guess = input("Guess a character: ").lower()

    # Check for valid input length
    if len(guess) != 1:
        print("Please enter a single character")
        continue
