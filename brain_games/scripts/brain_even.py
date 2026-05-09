import random

import prompt


def game(name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    max_rounds_count = 3
    for i in range(max_rounds_count):
        number = random.randint(1, 100)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
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