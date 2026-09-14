def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE!")
    print("Better luck next time!")
    exit(0)

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
        i += 1
    return True

def start1():
    xyz = []
    last = 0

    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')