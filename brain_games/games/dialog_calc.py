from brain_games.games.common import question
from brain_games.games.solution_verification import verification
import brain_games.config as config

from random import randint, choice

import prompt


def dialog(name: str, count: int = config.count) -> None:
    """
    Function for dialog with player
    in calculator play
    """

    while count:

        # brain
        numbers = [randint(0, config.max_value_calc) for _ in range(2)]

        actions = {
                  '*': numbers[0] * numbers[1],
                  '+': numbers[0] + numbers[1],
                  '-': numbers[0] - numbers[1],
        }

        punkt = choice('+-*')

        question(f'{numbers[0]} {punkt} {numbers[1]}')

        correct_answer = actions[punkt]
        user_answer = prompt.integer('Your answer: ')

        # проверка ответа
        result_verification = verification(
                                            name,
                                            correct_answer,
                                            user_answer
                                            )

        if result_verification:
            break

        count -= 1

    else:
        print(f"Congratulations, {name}!")
