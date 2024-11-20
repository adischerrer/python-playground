from datetime import datetime


def log_timestamp() -> None:
    print(f'Current date/time {datetime.now()}')


def greet(name: str) -> None:
    print(f'Hallo {name}')


def count_given_char(text: str, char: str) -> int:
    counter = 0
    for i in range(0, len(text)):
        if text[i] == char:
            counter += 1
    return counter


log_timestamp()
log_timestamp()
print("\n--------------------------------------------------------------------------------")
greet('Charly')
greet('Erika')
print("\n--------------------------------------------------------------------------------")
print(count_given_char("This is a test.", "s"))
print(count_given_char("This is a test.", "t"))
