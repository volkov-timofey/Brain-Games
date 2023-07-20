from brain_games.games.common import question
from random import randint, choice


QUESTION = 'What is the result of the expression?'
MAX_VALUE_CALC = 500


def initialize_correct_answer(max_value_calc=MAX_VALUE_CALC):
    """
    Correct answet for calc game
    """
    numbers = [randint(0, max_value_calc) for _ in range(2)]

    actions = {
        '*': numbers[0] * numbers[1],
        '+': numbers[0] + numbers[1],
        '-': numbers[0] - numbers[1],
    }

    punkt = choice('+-*')
    question(f'{numbers[0]} {punkt} {numbers[1]}')

    return actions[punkt]
