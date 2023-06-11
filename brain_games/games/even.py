import random


EXPLANATION = 'Answer "yes" if the number is even, otherwise answer "no".'
min = 1
max = 99


def get_step_data():
    random_number = random.randint(min, max)
    question = str(random_number)
    expected = 'yes' if random_number % 2 == 0 else 'no'

    return (question, expected)
