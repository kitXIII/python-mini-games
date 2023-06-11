import random
import math


EXPLANATION = 'Find the greatest common divisor of given numbers.'
min = 1
max = 99


def get_steps(count=3):
    steps = []
    for _ in range(count):
        num1 = random.randint(min, max)
        num2 = random.randint(min, max)

        steps.append((f"{num1} {num2}", str(math.gcd(num1, num2))))

    return steps
