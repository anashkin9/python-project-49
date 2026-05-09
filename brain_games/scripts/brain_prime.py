import random

import prompt

from brain_games.scripts.engine import run_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False 
    return True


def get_question():
    number = random.randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer


def game(name):
    run_game('Answer "yes" if given number is prime. Otherwise answer "no".',
             get_question, name)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)


if __name__ == "__main__":
    main()