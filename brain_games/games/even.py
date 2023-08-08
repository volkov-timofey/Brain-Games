from random import randint


MIN_VALUE_EVEN = 0
MAX_VALUE_EVEN = 500
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """
    check for even
    """
    return number % 2 == 0


def initialize_correct_answer():
    """
    Correct answet for even game
    """
    number = randint(MIN_VALUE_EVEN, MAX_VALUE_EVEN)

    return (
        number,
        'yes' if is_even(number) else 'no'
    )
