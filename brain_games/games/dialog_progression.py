from brain_games.games.common import question
from random import randint

import prompt


def dialog(name, count=3):

        while count:

            progression_numbers = [randint(0, 20)]
            diff = randint(2, 10)
            len_progression = randint(6, 10)
            random_position_unshow = randint(0, len_progression)
            
            # brain
            
            for i in range(len_progression):
                progression_numbers.append(progression_numbers[-1] + diff)
            
            correct_answer = progression_numbers[random_position_unshow]
            progression_numbers[random_position_unshow] = '..'
            
            question(' '.join([str(n) for n in progression_numbers]))

            user_answer = prompt.integer('Your answer: ')

            # проверка ответа
            flag = correct_answer == user_answer

            if flag:
                print("Correct!")
                count -= 1

            else:
                print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'."
                    f"\nLet's try again, {name}!"
                )
                break

        else:
            print(f"Congratulations, {name}!")
