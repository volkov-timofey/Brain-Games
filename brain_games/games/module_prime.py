from brain_games.games.common import question
from random import randint


MAX_VALUE_PRIME = 50
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simple_number(num: int) -> bool:
    """
    returns a flag of simplicity
    """

    divider = 2

    while divider < num:
        if num % divider == 0:
            return False

        divider += 1

    else:
        return True


def initialize_correct_answer(max_value_prime=MAX_VALUE_PRIME):
    """
    Correct answet for even prime
    """
    number = randint(2, max_value_prime)
    question(number)

    return "yes" if simple_number(number) else "no"
