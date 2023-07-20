from brain_games.games.solution_verification import verification
from brain_games.games.common import greetting
from brain_games.games import (
                                module_calc,
                                module_even,
                                module_gcd,
                                module_prime,
                                module_progression
                                )

import prompt


def engine(game: str, count: int = 3) -> None:

    modules = {
        'calc': module_calc,
        'even': module_even,
        'gcd': module_gcd,
        'prime': module_prime,
        'progression': module_progression,
        }

    param_game = modules[game]

    # greetting

    name = prompt.string('May I have your name? ')
    greetting(name)
    print(param_game.QUESTION)

    # questions
    while count:

        correct_answer = param_game.initialize_correct_answer()

        if game in ['prime', 'even']:
            user_answer = prompt.string('Your answer: ')
        else:
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
