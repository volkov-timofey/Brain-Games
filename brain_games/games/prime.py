from random import randint


MIN_VALUE_PRIME = 2
MAX_VALUE_PRIME = 50
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num: int) -> bool:
    """
    returns a flag of prime
    """
    divider = 2

    if num < 2:
        return False

    while divider < num:
        if num % divider == 0:
            return False

        divider += 1

    else:
        return True


def initialize_correct_answer():
    """
    Correct answet for even prime
    """
    number = randint(MIN_VALUE_PRIME, MAX_VALUE_PRIME)

    return (
        number,
        'yes' if is_prime(number) else 'no'
    )
