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
    failedd = 0

    for char in word:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_", end = " ")
            failed += 1

    
