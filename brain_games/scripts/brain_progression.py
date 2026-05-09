import random

import prompt

from brain_games.scripts.engine import run_game


def get_question():
    length = random.randint(5, 12)
    start = random.randint(1, 50)
    step = random.randint(1, 50)
    
    progression = list(range(start, start + length * step, step))
    
    hidden_item = random.choice(progression)
    index = progression.index(hidden_item)
    
    str_progression = [str(x) for x in progression]
    str_progression[index] = ".."
    
    question = ' '.join(str_progression)
    
    return question, hidden_item


def game(name):
    run_game('What number is missing in the progression?',
             get_question, name)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)


if __name__ == "__main__":
    main()