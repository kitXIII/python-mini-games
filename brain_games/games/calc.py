import random
from brain_games.runner import run_game

min = 1
max = 99


def get_step_data():
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)

    factor = random.randint(min, max) % 3

    match factor:
        case 0:
            return (f"{num1} + {num2}", str(num1 + num2))
        case 1:
            return (f"{num1} - {num2}", str(num1 - num2))
        case 2:
            return (f"{num1} * {num2}", str(num1 * num2))


def run():
    run_game('What is the result of the expression?', get_step_data)
