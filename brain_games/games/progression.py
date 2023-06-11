import random
from brain_games.runner import run_game

MIN_START = 1
MAX_START = 50
MIN_DELTA = 2
MAX_DELTA = 10
MIN_MEMBERS_COUNT = 5
MAX_MEMBERS_COUNT = 10


def get_step_data():
    start = random.randint(MIN_START, MAX_START)
    delta = random.randint(MIN_DELTA, MAX_DELTA)
    members_count = random.randint(MIN_MEMBERS_COUNT, MAX_MEMBERS_COUNT)

    members = []

    for i in range(members_count):
        members.append(str(start + i * delta))

    idx_of_hidden = random.randint(0, members_count - 1)

    hidden = members[idx_of_hidden]
    members[idx_of_hidden] = '..'

    return (' '.join(members), hidden)


def run():
    run_game(
        'What number is missing in the progression?',
        get_step_data
    )
