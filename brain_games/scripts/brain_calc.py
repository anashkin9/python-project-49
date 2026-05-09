import random

import prompt


def generate_expression() -> tuple:
    operations_list = ['+', '-', '*']
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(operations_list)
    match operation:
        case '+':
            expression = f'{number1} + {number2}'
            correct_answer = number1 + number2
            return (expression, correct_answer)
        case '-':
            expression = f'{number1} - {number2}'
            correct_answer = number1 - number2
            return (expression, correct_answer)
        case '*':
            expression = f'{number1} * {number2}'
            correct_answer = number1 * number2
            return (expression, correct_answer)


def game(name: str) -> None:
    print('What is the result of the expression?')
    max_rounds_count = 3
    for i in range(max_rounds_count):
        expression, correct_answer = generate_expression()
        print(f'Question: {expression}')
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