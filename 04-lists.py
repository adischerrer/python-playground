from shlex import split

names: list[str] = ['Luigi', 'Yvonne', 'Adi', 'Thomas', 'Gulia', 'Bob']
numbers: list[int] = [95, 74, 82, 15, 14, 3, 25, 4, 64, 75, 32, 12]

print('Normal order:   ', ', '.join(names))
print('Reversed order: ', ', '.join(names[::-1]))
print("\n--------------------------------------------------------------------------------")

# Sorted numbers greater than 40
print([num for num in sorted(numbers) if num > 40])
print("\n--------------------------------------------------------------------------------")

# first and last element from a list
# Logging of variable name and value in an elegant way
first, *_, last = names
print(f'{first=}, {last=}')
print("\n--------------------------------------------------------------------------------")


