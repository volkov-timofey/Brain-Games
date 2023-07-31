from brain_games.common import greetting

import prompt


ROUNDS_COUNT = 3


def initialize_game(module) -> None:

    # greetting

    name = prompt.string('May I have your name? ')
    greetting(name)
    print(module.QUESTION)

    global ROUNDS_COUNT

    # questions
    for i in range(ROUNDS_COUNT):

        question, correct_answer = module.initialize_correct_answer()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        # проверка ответа
        flag = str(correct_answer) == user_answer

        if flag:
            print('Correct!')

        else:
            print(
                f'{user_answer} is wrong answer ;(. '
                f'Correct answer was {correct_answer}.'
                f"\nLet's try again, {name}!"
            )
            break

    else:
        print(f'Congratulations, {name}!')
