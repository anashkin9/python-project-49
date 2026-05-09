import random

import prompt

import math

def game(name: str) -> None:
    print('Find the greatest common divisor of given numbers.')
    max_rounds_count = 3
    for i in range(max_rounds_count):
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        correct_answer = math.gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == int(user_answer):
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game(name)


if __name__ == "__main__":
    main()