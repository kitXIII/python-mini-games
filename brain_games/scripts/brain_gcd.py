#!/usr/bin/env python3


from brain_games.games.gcd import EXPLANATION, get_steps
from brain_games.runner import run_game


def main():
    run_game(EXPLANATION, get_steps())


if __name__ == '__main__':
    main()
