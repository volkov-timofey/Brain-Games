from brain_games.games.common import question
from random import randint


MAX_PROGR_NUM = 20
MAX_DIFF = 10
MIN_DIFF = 2
MAX_LEN = 10
MIN_LEN = 6
QUESTION = 'What number is missing in the progression?'


def initialize_correct_answer(
    max_progr_num=MAX_PROGR_NUM,
    min_diff=MIN_DIFF,
    max_diff=MAX_DIFF,
    min_len=MIN_LEN,
    max_len=MAX_LEN
):
    """
    Correct answet for even progression
    """

    progression_numbers = [randint(0, max_progr_num)]
    diff = randint(min_diff, max_diff)
    len_progression = randint(min_len, max_len)
    random_position_unshow = randint(0, len_progression)

    # brain

    for i in range(len_progression):
        progression_numbers.append(progression_numbers[-1] + diff)

    correct_answer = progression_numbers[random_position_unshow]
    progression_numbers[random_position_unshow] = '..'

    question(' '.join([str(n) for n in progression_numbers]))

    return correct_answer
