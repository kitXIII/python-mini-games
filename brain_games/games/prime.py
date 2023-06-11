import random
from brain_games.runner import run_game

min = 1
max = 99


def is_prime(number):
    if (number <= 2):
        return True

    half = number / 2
    current = 2

    while current < half:
        if number % current == 0:
            return False

        current += 1

    return True


def get_step_data():
    num = random.randint(min, max)
    expected = 'yes' if is_prime(num) else 'no'

    return (str(num), expected)


def run():
    run_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        get_step_data
    )
