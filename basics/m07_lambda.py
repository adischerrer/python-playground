names: list[str] = ['Zeno', 'Anna', 'Adi', 'Gulia', 'Amanda']

# Default implementation of min/max is alphabetical order
print(f'{min(names)=}')
print(f'{max(names)=}')
print("\n--------------------------------------------------------------------------------")

# Sort by length of the name
for name in names:
    print(f'Length of {name} = {len(name)}')
print("Shortest name: ", min(names, key=len))
print("Longest name:  ", max(names, key=len))
print("\n--------------------------------------------------------------------------------")

# Sort by number of "a" in the name
for name in names:
    print(f'a chars in {name} = {name.lower().count('a')}')
print("Least a chars in: ", min(names, key=lambda x: x.lower().count('a')))
print("Most a chars in:  ", max(names, key=lambda x: x.lower().count('a')))
print("\n--------------------------------------------------------------------------------")


def my_map(func, input_list: list) -> list:
    result: list = []
    for elem in input_list:
        result.append(func(elem))
    return result


print(my_map(lambda x: x + 1, [1, 2, 3, 4]))
print(my_map(lambda x: x ** 3, [1, 2, 3, 4]))
print(my_map(lambda x: len(x), ['one', 'two', 'three']))
