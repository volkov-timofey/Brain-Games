def verification(name: str, correct_answer, user_answer) -> None:
    """
    Verification user's answer
    """

    flag = correct_answer == user_answer

    if flag:
        print("Correct!")

    else:
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
            f"\nLet's try again, {name}!"
        )
        return True
