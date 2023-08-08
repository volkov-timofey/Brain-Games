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

    step = randint(MIN_DIFF, MAX_DIFF)
    len_progression = randint(MIN_LEN, MAX_LEN)
    begin_number = randint(MIN_PROGR_NUM, MAX_PROGR_NUM)
    end_number = begin_number + (len_progression * step)

    # len_progression is variable, than UNSHOW_END I didn't use
    random_position_unshow = randint(UNSHOW_START, len_progression - 1)

    # brain
    progression_numbers = [num for num in range(begin_number, end_number, step)]

    correct_answer = progression_numbers[random_position_unshow]
    progression_numbers[random_position_unshow] = '..'

    question = ' '.join([str(n) for n in progression_numbers])

    return (question, correct_answer)
