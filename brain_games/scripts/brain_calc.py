# brain_calc.py
import random
import prompt
from brain_games.scripts.engine import run_game

OPS = {'+': lambda a, b: a + b,
       '-': lambda a, b: a - b,
       '*': lambda a, b: a * b}

def get_question():
    a, b = random.randint(1, 100), random.randint(1, 100)
    op = random.choice(list(OPS))
    return f'{a} {op} {b}', OPS[op](a, b)

def game(name):
    run_game('What is the result of the expression?', get_question, name)

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)

if __name__ == "__main__":
    main()