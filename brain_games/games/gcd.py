import random
import math
from brain_games.runner import run_game

MIN = 1
MAX = 99


def get_step_data():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)

    return (f"{num1} {num2}", str(math.gcd(num1, num2)))


def run():
    run_game(
        'Find the greatest common divisor of given numbers.',
        get_step_data
    )
