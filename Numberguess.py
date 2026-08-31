import random

BANNER = """
  █   █  █   █  █   █  ████   █████  ████ 
  ██  █  █   █  ██ ██  █   █  █      █   █
  █ █ █  █   █  █ █ █  ████   ████   ████ 
  █  ██  █   █  █   █  █   █  █      █  █ 
  █   █   ███   █   █  ████   █████  █   █

   ████  █   █  █████   ████   ████
  █      █   █  █      █      █    
  █  ██  █   █  ████    ███    ███ 
  █   █  █   █  █          █      █
   ███    ███   █████  ████   ████
"""


def draw_chances(used, total):
    """Show remaining chances as a row of hearts."""
    left = total - used
    return '  Chances: ' + ('♥ ' * left) + ('· ' * used) + f' ({left} left)'


def draw_range(low, high, guess):
    """Draw the guess on a number line between low and high."""
    width = 40
    span = high - low if high > low else 1
    pos = int((guess - low) / span * (width - 1))
    pos = max(0, min(width - 1, pos))
    line = ['-'] * width
    line[pos] = '^'
    return f'  {low} |' + ''.join(line) + f'| {high}'


print(BANNER)
print("Hello!, Welcome to the Number Guessing Game. \n You have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}")

num = random.randint(low, high)

# Total allowed chances
ch = 7

# Guess Counter
gc = 0

while gc < ch:
    print(draw_chances(gc, ch))
    gc += 1
    guess = int(input('Enter your guess: '))

    print(draw_range(low, high, guess))

    if guess == num:
        print('  ***  ')
        print(' * ! * ')
        print('  ***  ')
        print(f'Correct! The number is {num} You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! that number was {num} Better luck next time.')

    elif guess > num:
        print('Too High! Try a lower number.  v')

    elif guess < num:
        print('Too low! Try a higher number.  ^')
