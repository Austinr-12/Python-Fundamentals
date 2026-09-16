import sys
import time

# ANSI color codes for nicer terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

TARGET = 21


def banner():
    print(CYAN + BOLD)
    print("╔══════════════════════════════════════╗")
    print("║         THE 21 NUMBER GAME           ║")
    print("╚══════════════════════════════════════╝" + RESET)
    print("Take turns counting up from 1.")
    print("On each turn, say 1, 2, or 3 numbers in a row.")
    print(f"Whoever is forced to say {BOLD}{TARGET}{RESET} loses!\n")
    print(f"{CYAN}■ You{RESET}   {RED}■ Computer{RESET}\n")


def show_board(said):
    """Print numbers 1-21 in a grid, colored by who said each one."""
    print()
    for n in range(1, TARGET + 1):
        if n in said:
            color = CYAN if said[n] == "you" else RED
            cell = f"{color}{BOLD}{n:>3}{RESET}"
        else:
            cell = f"{DIM}{n:>3}{RESET}"
        end = "\n" if n % 7 == 0 else " "
        print(cell, end=end)
    print()


def ask_int(prompt, low, high):
    """Keep asking until the user enters a whole number between low and high."""
    while True:
        answer = input(prompt).strip()
        if answer.isdigit() and low <= int(answer) <= high:
            return int(answer)
        print(f"{YELLOW}Please enter a number from {low} to {high}.{RESET}")


def computer_move(last):
    """Try to land on a multiple of 4 (4, 8, 12, 16, 20)."""
    count = 4 - (last % 4)
    if count == 4:  # already on a multiple of 4, no winning move
        count = 1
    return min(count, TARGET - last)


def say_numbers(said, last, count, who):
    numbers = list(range(last + 1, last + count + 1))
    for n in numbers:
        said[n] = who
    color = CYAN if who == "you" else RED
    name = "You" if who == "you" else "Computer"
    print(f"{color}{BOLD}{name} said: {', '.join(map(str, numbers))}{RESET}")
    return numbers[-1]


def play():
    said = {}
    last = 0

    choice = ""
    while choice not in ("F", "S"):
        choice = input("Go (F)irst or (S)econd? > ").strip().upper()
    turn = "you" if choice == "F" else "computer"

    while last < TARGET:
        show_board(said)
        if turn == "you":
            max_count = min(3, TARGET - last)
            options = "1" if max_count == 1 else f"1-{max_count}"
            count = ask_int(f"Your turn! How many numbers ({options})? > ",
                            1, max_count)
            last = say_numbers(said, last, count, "you")
            if last == TARGET:
                show_board(said)
                print(f"{RED}{BOLD}You said {TARGET}. YOU LOSE!{RESET}")
                print("Better luck next time!\n")
                return
            turn = "computer"
        else:
            print(f"{DIM}Computer is thinking...{RESET}")
            time.sleep(0.8)
            last = say_numbers(said, last, computer_move(last), "computer")
            if last == TARGET:
                show_board(said)
                print(f"{GREEN}{BOLD}Computer said {TARGET}. "
                      f"CONGRATULATIONS, YOU WON!{RESET}\n")
                return
            turn = "you"


def main():
    banner()
    while True:
        answer = input("Do you want to play? (yes/no) > ").strip().lower()
        if answer in ("yes", "y"):
            play()
        elif answer in ("no", "n"):
            print("Thanks for playing! Goodbye.")
            sys.exit(0)
        else:
            print(f"{YELLOW}Please type yes or no.{RESET}")


if __name__ == "__main__":
    main()
