import random

words = ["apple", "banana", "mango", "orange", "grapes", "papaya"]

word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")
print("Hint: The word is a fruit.")

while wrong_guesses < max_attempts:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_"

    print(hangman[wrong_guesses])
    print("Word:", display)