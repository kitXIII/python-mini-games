import random
from brain_games.runner import run_game

MIN = 1
MAX = 99


def get_step_data():
    arg1 = random.randint(MIN, MAX)
    arg2 = random.randint(MIN, MAX)

    factor = random.randint(MIN, MAX) % 3

    match factor:
        case 0:
            return (f"{arg1} + {arg2}", str(arg1 + arg2))
        case 1:
            return (f"{arg1} - {arg2}", str(arg1 - arg2))
        case 2:
            return (f"{arg1} * {arg2}", str(arg1 * arg2))


def run():
    run_game('What is the result of the expression?', get_step_data)
