#!/usr/bin/env python3

from brain_games.engine import initialize_game
import brain_games.games.even as even


def main():

    initialize_game(even)


if __name__ == '__main__':
    main()
