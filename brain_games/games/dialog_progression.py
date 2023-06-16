from brain_games.games.common import question
from brain_games.games.solution_verification import verification
import brain_games.config as config

from random import randint

import prompt


def dialog(name: str, count: int = config.count) -> None:
    """
    Function for dialog with player
    in progression play
    """

    while count:

        progression_numbers = [randint(0, config.max_progr_num)]
        diff = randint(config.min_diff, config.max_diff)
        len_progression = randint(config.min_len, config.max_len)
        random_position_unshow = randint(0, len_progression)

        # brain

        for i in range(len_progression):
            progression_numbers.append(progression_numbers[-1] + diff)

        correct_answer = progression_numbers[random_position_unshow]
        progression_numbers[random_position_unshow] = '..'

        question(' '.join([str(n) for n in progression_numbers]))

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
