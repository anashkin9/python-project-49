import prompt

MAX_ROUNDS = 3


def run_game(description: str, get_question_answer, name: str) -> None:
    print(description)
    for _ in range(MAX_ROUNDS):
        question, correct_answer = get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')