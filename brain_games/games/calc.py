import random


EXPLANATION = 'What is the result of the expression?'
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
