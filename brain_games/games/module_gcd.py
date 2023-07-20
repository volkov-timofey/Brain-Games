from brain_games.games.common import question
from random import randint


QUESTION = 'Find the greatest common divisor of given numbers.'
MAX_VALUE_GCD = 100


def nod(num1: int, num2: int) -> int:
    """
    return nod 2 integer
    """

    if num2 == 0:
        return num1
    else:
        return nod(num2, num1 % num2)


def initialize_correct_answer(max_value_gcd=MAX_VALUE_GCD):
    """
    Correct answet for even gcd
    """
    numbers = [randint(0, max_value_gcd) for _ in range(2)]
    question(f'{numbers[0]} {numbers[1]}')

    return nod(numbers[0], numbers[1])
