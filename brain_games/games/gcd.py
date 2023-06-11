import random
import math


EXPLANATION = 'Find the greatest common divisor of given numbers.'
min = 1
max = 99


def get_step_data():
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)

    return (f"{num1} {num2}", str(math.gcd(num1, num2)))
