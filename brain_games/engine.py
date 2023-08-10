import prompt


ROUNDS_COUNT = 3


def initialize_game(game_module) -> None:

    # greetting

    name = prompt.string('May I have your name? ')
    print('Welcome to the Brain Games!')
    print(f'Hello, {name}!')
    print(game_module.QUESTION)

    # questions
    for i in range(ROUNDS_COUNT):

        question, correct_answer = game_module.initialize_correct_answer()

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
