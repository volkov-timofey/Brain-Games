from brain_games.games.common import question
from random import randint


MAX_VALUE_EVEN = 500
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def initialize_correct_answer(max_value_even=MAX_VALUE_EVEN):
    """
    Correct answet for even game
    """
    number = randint(0, max_value_even)
    question(number)

    return "yes" if number % 2 == 0 else "no"
