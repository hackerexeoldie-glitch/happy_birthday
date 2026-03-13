import random
import time
import sys
import os

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'bold': '\033[1m',
}

RAINBOW = [COLORS['red'], COLORS['yellow'], COLORS['green'], 
           COLORS['cyan'], COLORS['blue'], COLORS['magenta']]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_rainbow(text, delay=0.08):
    for i, char in enumerate(text):
        color = RAINBOW[i % len(RAINBOW)]
        sys.stdout.write(f"{color}{char}")
        sys.stdout.flush()
        time.sleep(delay)
    print(COLORS['reset'])

def print_confetti_banner(name):
    clear_screen()
    time.sleep(0.4)
    
    print("\n" + COLORS['yellow'] + "═" * 60 + COLORS['reset'])
    print_rainbow("🎉 HAPPY BIRTHDAY 🎉", delay=0.05)
    time.sleep(0.3)
    print_rainbow(f"      {name.upper()}!      ", delay=0.07)
    print("\n" + COLORS['cyan'] + "Have an incredible day full of joy, cake, love & awesome moments!" + COLORS['reset'])
    print(COLORS['magenta'] + "\n 🥳 🎂 🎈 ✨ 🎁 🌟 " * 4 + COLORS['reset'])
    print(COLORS['yellow'] + "═" * 60 + COLORS['reset'] + "\n")

def ask_birthday_equation(player_name):
    # Randomly choose operation: + , × , or ÷ (exact division)
    op = random.choice(['+', '×', '÷'])
    
    if op == '+':
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        correct = a + b
        question = f"{a} + {b}"
    
    elif op == '×':
        a = random.randint(1, 50)
        b = random.randint(1, 12)   # keep multiplication reasonable
        correct = a * b
        question = f"{a} × {b}"
    
    else:  # division - exact only
        b = random.randint(2, 25)   # divisor
        mult = random.randint(2, 12)  # multiplier to keep result ≤ 50*12-ish
        a = b * mult                # dividend = divisor × multiplier
        correct = mult              # result = multiplier
        question = f"{a} ÷ {b}"
    
    print(f"\n{COLORS['yellow']}{COLORS['bold']}Final step to unlock your surprise!{COLORS['reset']}")
    print(f"{COLORS['cyan']}Quick math — what's the answer?{COLORS['reset']}")
    print(f"\n  {COLORS['bold']}{question} = ?{COLORS['reset']}")
    
    try:
        answer = int(input(f"\n{COLORS['magenta']}Your answer: {COLORS['reset']}").strip())
        if answer == correct:
            print(f"\n{COLORS['green']}{COLORS['bold']}Perfect! Here’s your birthday surprise! 🎉{COLORS['reset']}")
            time.sleep(0.7)
            print_confetti_banner(player_name)
        else:
            print(f"\n{COLORS['red']}Sorry... the correct answer was {correct}{COLORS['reset']}")
            print(f"{COLORS['yellow']}Happy birthday anyway, {player_name}! Hope you have a fantastic day! 🎂{COLORS['reset']}")
    except ValueError:
        print(f"\n{COLORS['red']}That wasn't a number...{COLORS['reset']}")
        print(f"The answer was {correct}. Wishing you a very happy birthday, {player_name}! 🥳")

def number_guessing_game(player_name):
    clear_screen()
    time.sleep(0.3)
    
    print(f"\n{COLORS['cyan']}{COLORS['bold']}Alright {player_name} — number guessing time!{COLORS['reset']}\n")
    print(f"{COLORS['yellow']}Select difficulty:{COLORS['reset']}")
    print(f"  {COLORS['green']}1 → Easy    (1–20, 6 attempts){COLORS['reset']}")
    print(f"  {COLORS['yellow']}2 → Medium  (1–50, 7 attempts){COLORS['reset']}")
    print(f"  {COLORS['red']}3 → Hard    (1–100, 8 attempts){COLORS['reset']}")
    
    while True:
        level = input(f"\n{COLORS['magenta']}Choose (1/2/3): {COLORS['reset']}").strip()
        if level in ["1", "2", "3"]:
            break
        print(f"{COLORS['red']}Please enter 1, 2 or 3{COLORS['reset']}")

    level = int(level)
    
    if level == 1:
        max_num, max_attempts, diff = 20, 6, f"{COLORS['green']}Easy{COLORS['reset']}"
    elif level == 2:
        max_num, max_attempts, diff = 50, 7, f"{COLORS['yellow']}Medium{COLORS['reset']}"
    else:
        max_num, max_attempts, diff = 100, 8, f"{COLORS['red']}Hard{COLORS['reset']}"

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\n→ {diff} mode ←")
    print(f"{COLORS['cyan']}I'm thinking of a number between 1 and {max_num}...{COLORS['reset']}")
    print(f"You have {max_attempts} attempts. Let's go!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"{COLORS['blue']}Attempt {attempts+1}/{max_attempts} → {COLORS['reset']}"))
            attempts += 1

            if guess == secret_number:
                print(f"\n{COLORS['green']}{COLORS['bold']}🎈 Spot on! You got it in {attempts} tries! 🎈{COLORS['reset']}")
                print(f"{COLORS['yellow']}Number was {secret_number}{COLORS['reset']}")
                time.sleep(0.6)
                print_rainbow("Well done! 🏆", delay=0.07)
                return True
            elif guess < secret_number:
                print(f"{COLORS['cyan']}Too low ↑{COLORS['reset']}")
            else:
                print(f"{COLORS['magenta']}Too high ↓{COLORS['reset']}")

            if attempts >= max_attempts - 2 and attempts < max_attempts:
                low = max(1, secret_number - 10)
                high = min(max_num, secret_number + 10)
                print(f"  {COLORS['yellow']}(hint: between {low}–{high}){COLORS['reset']}")

        except ValueError:
            print(f"{COLORS['red']}Please enter a number{COLORS['reset']}")
            continue

    print(f"\n{COLORS['red']}Game over! The number was {secret_number}{COLORS['reset']}")
    return False

def main():
    clear_screen()
    time.sleep(0.3)
    
    print(f"{COLORS['magenta']}{COLORS['bold']}Welcome! 🎂{COLORS['reset']}\n")
    
    name = input(f"{COLORS['cyan']}What's your name? {COLORS['reset']}").strip()
    if not name:
        name = "Birthday Star"
    
    PLAYER_NAME = name.title()

    while True:
        play = input(
            f"\n{COLORS['yellow']}{PLAYER_NAME}, want to play again? (y/n): {COLORS['reset']}"
        ).lower().strip()
        
        if play in ['n', 'no', 'q', 'quit', 'exit', '']:
            ask_birthday_equation(PLAYER_NAME)
            break

        elif play in ['y', 'yes', 'ok', 'sure', '']:
            number_guessing_game(PLAYER_NAME)
            continue

        else:
            print(f"{COLORS['red']}Just type y or n please{COLORS['reset']}")

if __name__ == "__main__":
    main()
