# brain_gcd.py
import random, math
import prompt
from brain_games.scripts.engine import run_game

def get_question():
    a, b = random.randint(1, 100), random.randint(1, 100)
    return f'{a} {b}', math.gcd(a, b)

def game(name):
    run_game('Find the greatest common divisor of given numbers.',
             get_question, name)

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)

if __name__ == "__main__":
    main()