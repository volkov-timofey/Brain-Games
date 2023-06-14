#!/usr/bin/env python3

from brain_games.games.common import greetting
from brain_games.games.dialog_even import dialog

import prompt


def main():

    name = prompt.string('May I have your name? ')
    greetting(name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    dialog(name)


if __name__ == "__main__":
    main()