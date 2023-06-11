import prompt
from brain_games import cli


def run_game(explanation, steps):
    name = cli.welcome_user()
    print(explanation)

    for (question, expected) in steps:
        answer = prompt.string(
            f'Question: {question}\nYour answer: ', empty=True)

        if answer is None:
            answer = 'Empty answer'

        if (answer != expected):
            print("'{0}' is wrong answer ;(. "
                  "Correct answer was '{1}'.\n"
                  "Let's try again, {2}!".format(answer, expected, name))
            return

        print('Correct!')

    print(f'Congratulations, {name}!')
