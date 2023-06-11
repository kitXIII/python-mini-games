import random
from brain_games.runner import run_game

min = 1
max = 99


def get_step_data():
    random_number = random.randint(min, max)
    question = str(random_number)
    expected = 'yes' if random_number % 2 == 0 else 'no'

    return (question, expected)


def run():
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        get_step_data
    )
