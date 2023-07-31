from random import randint, choice


MIN_VALUE_CALC = 0
MAX_VALUE_CALC = 500
QUESTION = 'What is the result of the expression?'


def initialize_correct_answer():
    """
    Correct answet for calc game
    """
    number1 = randint(MIN_VALUE_CALC, MAX_VALUE_CALC)
    number2 = randint(MIN_VALUE_CALC, MAX_VALUE_CALC)

    actions = {
        '*': number1 * number2,
        '+': number1 + number2,
        '-': number1 - number2,
    }

    operation = choice('+-*')
    question = f'{number1} {operation} {number2}'

    return (question, actions[operation])
