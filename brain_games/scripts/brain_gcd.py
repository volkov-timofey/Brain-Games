#!/usr/bin/env python3

from brain_games.games.common import greetting
from brain_games.games.dialog_gcd import dialog

import prompt


def main():

    name = prompt.string('May I have your name? ')
    greetting(name)
    print('Find the greatest common divisor of given numbers.')
    dialog(name)


if __name__ == "__main__":
    main()
