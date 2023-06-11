#!/usr/bin/env python3

from random import randint
import prompt


def main():

    def greetting(name) -> None:
        """
        Greetting
        """
        print("Welcome to the Brain Games!")
        print(f"Hello, {name}!")
        print('Answer "yes" if the number is even, otherwise answer "no".')

    def question(number):
        """
        question number is even
        """
        print(f'Question: {number}')

    def dialog(name, count=3):

        while count:

            number = randint(0, 500)

            question(number)

            correct_answer = "yes" if number % 2 == 0 else "no"
            user_answer = prompt.string('Your answer: ')

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

    name = prompt.string('May I have your name? ')
    greetting(name)
    dialog(name)


if __name__ == "__main__":
    main()
