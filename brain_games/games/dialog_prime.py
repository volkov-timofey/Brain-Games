from brain_games.games.common import question
from brain_games.games.simple_number import simple_number
from brain_games.games.solution_verification import verification
import brain_games.config as config

from random import randint

import prompt


def dialog(name: str, count: int = config.count) -> None:
    """
    Function for dialog with player
    in prime play
    """

    while count:

        number = randint(0, config.max_value_prime)

        question(number)

        correct_answer = "yes" if simple_number(number) else "no"
        user_answer = prompt.string('Your answer: ')

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
