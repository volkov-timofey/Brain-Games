def simple_number(num: int) -> bool:
    """
    returns a flag of simplicity
    """

    divider = 2

    while divider < num:
        if num % divider == 0:
            return False

        divider += 1

    else:
        return True
