import prompt
from brain_games import cli


COUNT_OF_STEPS = 3


def run_game(explanation, get_step_data):
    name = cli.welcome_user()
    print(explanation)

    for _ in range(COUNT_OF_STEPS):
        question, expectation = get_step_data()

        answer = prompt.string(
            f'Question: {question}\nYour answer: ', empty=True)

        if answer is None:
            answer = 'Empty answer'

        if (answer != expectation):
            print("'{0}' is wrong answer ;(. "
                  "Correct answer was '{1}'.\n"
                  "Let's try again, {2}!".format(answer, expectation, name))
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
