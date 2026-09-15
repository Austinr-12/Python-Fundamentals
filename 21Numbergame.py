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

    if chance.upper() == "F":
        while True:
            if last == 20:
                lose1()
                print("\nYour Turn.")
                inp = int(input("How many numbers do you wish" \
                "to enter (1-3)\n> "))

                if 1 <= inp <= 3:
                    comp = 4 - inp
                else:
                    print("Wrong input. You are disqualified from " \
                    "the game.")
                    lose1()

                print("Enter your numbers:")
                for _ in range(inp):
                    xyz.append(int(input('>')))

                last = xyz[-1]

                if not check(xyz):
                    print("\nYou did not enter consecutive integers.")
                    lose1()

                if last == 21:
                    lose1()
