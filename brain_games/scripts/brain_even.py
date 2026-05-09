import random
import prompt
from brain_games.scripts.engine import run_game

def get_question():
    number = random.randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer

def game(name):
    run_game('Answer "yes" if the number is even, otherwise answer "no".',
             get_question, name)

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)

if __name__ == "__main__":
    main()