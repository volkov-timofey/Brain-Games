from brain_games.games.common import question
from random import randint, choice

import prompt


def dialog(name, count=3):

        while count:

            
            # brain
            numbers = [randint(0, 500) for _ in range(2)]
            
            actions = {
                      '*' : numbers[0] * numbers[1],
                      '+' : numbers[0] + numbers[1],
                      '-' : numbers[0] - numbers[1],
            }
            
            punkt = choice('+-*')
            
            question(f'{numbers[0]} {punkt} {numbers[1]}')

            correct_answer = actions[punkt]
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
