import prompt


def welcome_user():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ', empty=True)

    if name is None:
        name = 'Noname'

    print(f'Hello, {name}')

    return name
