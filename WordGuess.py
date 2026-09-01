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

