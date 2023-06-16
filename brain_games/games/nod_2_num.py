def nod(num1: int, num2: int) -> int:
    """
    return nod 2 integer
    """

    if num2 == 0:
        return num1
    else:
        return nod(num2, num1 % num2)
