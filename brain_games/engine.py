import prompt


ROUNDS_COUNT = 3


# комментрий от 31.07 "название функции должно быть глаголом"
def game_module(module) -> None:

    # greetting

    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!')
    print(f'Hello, {name}!')
    print(module.QUESTION)

    # questions
    for i in range(ROUNDS_COUNT):

        question, correct_answer = module.initialize_correct_answer()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        # check an answer
        is_answer_correct = str(correct_answer) == user_answer

        if is_answer_correct:
            print('Correct!')

        else:
            print(
                f'{user_answer} is wrong answer ;(. '
                f'Correct answer was {correct_answer}.'
                f"\nLet's try again, {name}!"
            )
            break

    else:
        print(f'Congratulations, {name}!')
