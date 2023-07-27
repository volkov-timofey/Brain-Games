from random import randint


MIN_VALUE_EVEN = 0
MAX_VALUE_EVEN = 500
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def initialize_correct_answer():
    """
    Correct answet for even game
    """
    number = randint(MIN_VALUE_EVEN, MAX_VALUE_EVEN)
    print(f'Question: {number}')

    return 'yes' if number % 2 == 0 else 'no'
