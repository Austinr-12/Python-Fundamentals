import sys
import time

# ANSI codes for nicer terminal output
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
REVERSE = "\033[7m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

TARGET = 21
WIDTH = 36  # inside width of every box
COLORS = {"you": CYAN, "computer": RED}
NAMES = {"you": "You", "computer": "Computer"}


def clear_screen():
    print("\033[2J\033[H", end="")


def box(lines, color):
    """Print lines centered inside a double-line box."""
    print(color + BOLD + "  ╔" + "═" * WIDTH + "╗")
    for line in lines:
        print("  ║" + line.center(WIDTH) + "║")
    print("  ╚" + "═" * WIDTH + "╝" + RESET)


def intro():
    clear_screen()
    print()
    box(["THE 21 NUMBER GAME"], CYAN)
    print()
    print("  Take turns counting up from 1.")
    print("  On each turn, say 1, 2, or 3 numbers.")
    print(f"  Whoever is forced to say {BOLD}{TARGET}{RESET} loses!")
    print()


def show_score(score):
    print(f"  {CYAN}{BOLD}You {score['you']}{RESET}"
          f"  {DIM}vs{RESET}  "
          f"{RED}{BOLD}Computer {score['computer']}{RESET}")


def show_board(said, recent):
    """Numbers 1-21 in a grid, colored by who said them; latest move highlighted."""
    print("  ┌" + "─" * WIDTH + "┐")
    for row_start in range(1, TARGET + 1, 7):
        cells = []
        for n in range(row_start, row_start + 7):
            if n in said:
                style = COLORS[said[n]] + BOLD
                if n in recent:
                    style += REVERSE
            else:
                style = DIM
            cells.append(f"{style} {n:>2} {RESET}")
        print("  │ " + " ".join(cells) + " │")
    print("  └" + "─" * WIDTH + "┘")


def show_progress(last):
    """A bar that turns from green to yellow to red as the count nears 21."""
    if last >= 17:
        color = RED
    elif last >= 13:
        color = YELLOW
    else:
        color = GREEN
    bar = color + "█" * last + RESET + DIM + "░" * (TARGET - last) + RESET
    print(f"  Count  {bar}  {BOLD}{last:>2}/{TARGET}{RESET}")


def render(said, recent, last, score, log):
    clear_screen()
    print()
    box(["THE 21 NUMBER GAME"], CYAN)
    show_score(score)
    print()
    show_board(said, recent)
    show_progress(last)
    print()
    for line in log[-3:]:  # the last few moves
        print("  " + line)
    print()


def ask_int(prompt, low, high):
    """Keep asking until the user enters a whole number between low and high."""
    while True:
        answer = input(prompt).strip()
        if answer.isdigit() and low <= int(answer) <= high:
            return int(answer)
        print(f"  {YELLOW}Please enter a number from {low} to {high}.{RESET}")


def computer_move(last):
    """Try to land on a multiple of 4 (4, 8, 12, 16, 20)."""
    count = 4 - (last % 4)
    if count == 4:  # already on a multiple of 4, no winning move
        count = 1
    return min(count, TARGET - last)


def thinking():
    print(f"  {DIM}Computer is thinking", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(RESET)


def play(score):
    said = {}
    recent = []
    log = []
    last = 0

    render(said, recent, last, score, log)
    choice = ""
    while choice not in ("F", "S"):
        choice = input("  Go (F)irst or (S)econd? > ").strip().upper()
    turn = "you" if choice == "F" else "computer"

    while last < TARGET:
        render(said, recent, last, score, log)
        if turn == "you":
            max_count = min(3, TARGET - last)
            options = "1" if max_count == 1 else f"1-{max_count}"
            count = ask_int(f"  Your turn! How many numbers ({options})? > ",
                            1, max_count)
            recent = list(range(last + 1, last + count + 1))
            for n in recent:
                said[n] = "you"
            last = recent[-1]
        else:
            thinking()
            count = computer_move(last)
            recent = []
            for n in range(last + 1, last + count + 1):  # reveal one at a time
                said[n] = "computer"
                recent.append(n)
                last = n
                render(said, recent, last, score, log)
                time.sleep(0.35)

        numbers = ", ".join(map(str, recent))
        log.append(f"{COLORS[turn]}{BOLD}{NAMES[turn]:>8}{RESET} said {numbers}")
        turn = "computer" if turn == "you" else "you"

    # Whoever just said 21 lost, so the player whose turn it is now wins
    winner = turn
    score[winner] += 1
    render(said, recent, last, score, log)
    if winner == "you":
        box(["YOU WIN!", "The computer said 21."], GREEN)
    else:
        box(["YOU LOSE!", "You said 21.", "Better luck next time!"], RED)
    print()


def main():
    score = {"you": 0, "computer": 0}
    intro()
    prompt = "  Ready to play? (yes/no) > "
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            play(score)
            prompt = "  Play again? (yes/no) > "
        elif answer in ("no", "n"):
            print()
            show_score(score)
            print("  Thanks for playing! Goodbye.\n")
            sys.exit(0)
        else:
            print(f"  {YELLOW}Please type yes or no.{RESET}")


if __name__ == "__main__":
    main()
