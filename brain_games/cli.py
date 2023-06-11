import prompt


def welcome_user():
    name = prompt.string('May I have your name? ', empty=True)

    if name is None:
        name = 'Noname'

    print(f'Hello, {name}')

    return name
