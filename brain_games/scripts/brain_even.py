#!/usr/bin/env python3


from brain_games.games.even import EXPLANATION, get_step_data
from brain_games.runner import run_game


def main():
    run_game(EXPLANATION, get_step_data)


if __name__ == '__main__':
    main()
