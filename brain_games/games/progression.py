import random
from brain_games.runner import run_game

min_start = 1
max_start = 50
min_delta = 2
max_delta = 10
min_members_count = 5
max_members_count = 10


def get_step_data():
    start = random.randint(min_start, max_start)
    delta = random.randint(min_delta, max_delta)
    members_count = random.randint(min_members_count, max_members_count)

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
