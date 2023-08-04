from random import randint


UNSHOW_START = 0
MIN_PROGR_NUM = 0
MAX_PROGR_NUM = 20
MAX_DIFF = 10
MIN_DIFF = 2
MAX_LEN = 10
MIN_LEN = 6
QUESTION = 'What number is missing in the progression?'


def initialize_correct_answer():
    """
    Correct answet for even progression
    """

    progression_numbers = [randint(MIN_PROGR_NUM, MAX_PROGR_NUM)]
    diff = randint(MIN_DIFF, MAX_DIFF)
    len_progression = randint(MIN_LEN, MAX_LEN)

    # len_progression is variable, than UNSHOW_END I didn't use
    random_position_unshow = randint(UNSHOW_START, len_progression)

    # brain
    for i in range(len_progression):
        progression_numbers.append(progression_numbers[-1] + diff)

    correct_answer = progression_numbers[random_position_unshow]
    progression_numbers[random_position_unshow] = '..'

    question = f"{' '.join([str(n) for n in progression_numbers])}"

    return (question, correct_answer)
