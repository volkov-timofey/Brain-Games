from brain_games.games.common import greetting

import prompt


ROUNDS_COUNT = 3


def engine(module) -> None:

    # greetting

    name = prompt.string('May I have your name? ')
    greetting(name)
    print(module.QUESTION)

    global ROUNDS_COUNT

    # questions
    while ROUNDS_COUNT:

        correct_answer = module.initialize_correct_answer()

        user_answer = prompt.string('Your answer: ')

        # проверка ответа
        result_verification = verification(
            name,
            correct_answer,
            user_answer
        )

        if result_verification:
            break

        ROUNDS_COUNT -= 1

    else:
        print(f'Congratulations, {name}!')


def verification(name: str, correct_answer, user_answer) -> None:
    """
    Verification user's answer
    """

    flag = str(correct_answer) == user_answer

    if flag:
        print('Correct!')

    else:
        print(
            f'{user_answer} is wrong answer ;(. '
            f'Correct answer was {correct_answer}.'
            f"\nLet's try again, {name}!"
        )
        return True
