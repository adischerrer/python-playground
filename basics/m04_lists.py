names: list[str] = ['Luigi', 'Yvonne', 'Adi', 'Thomas', 'Gulia', 'Bob']
numbers: list[int] = [95, 74, 82, 15, 14, 3, 25, 4, 64, 75, 32, 12]

print(f'Normal list style:            {names}')
print('Print names nicely formatted: ', end='')
print(*names, sep=' - ', end='.\n')
print('Normal order:                ', ', '.join(names))
print('Reversed order:              ', ', '.join(names[::-1]))
print("\n--------------------------------------------------------------------------------")

print(f'{numbers=}')
print('Sorted numbers greater than 40')
print([num for num in sorted(numbers) if num > 40])
print("\n--------------------------------------------------------------------------------")

# first and last element from a list
# Logging of variable name and value in an elegant way
first, *_, last = names
print(f'{first=}, {last=}')
print("\n--------------------------------------------------------------------------------")
