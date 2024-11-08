print('This is a test')
print('Info without a CR at ', end='')
print('the end')
print("Double quotes can be used as well")
print("some", "elements", 'printed', 'with', 'special', 'separator', sep='---')
print("\n--------------------------------------------------------------------------------")

a = 11
b: int = 88  # Type annotation are not mandatory but help a lot. They have NO effect in the program but only
print("Result of", a, "+", b, "=", a + b)
print(f'Result of {a} + {b} = {a + b}')  # Immediate evaluation when using f'xyz {}'
print("\n--------------------------------------------------------------------------------")

# Data types
my_int: int = 123
my_float: float = 1.23
my_str: str = 'Any text'
my_bool: bool = True

my_list: list[int] = [1, 2, 3]
my_tuples: tuple[str, float] = ('Bob', -3.5)  # Immutable!
my_set: set = {9, 6, 12, 6}  # No duplicates
my_dict: dict = {'name': 'Bob', 'age': 20}  # List of Key/Value pairs
print("int:", my_int)
print("float:", my_float)
print("str:", my_str)
print("bool:", my_bool)
print("list:", my_list)
print("set:", my_set)
print("dict:", my_dict)
print("\n--------------------------------------------------------------------------------")

# If/else in a one-liner
number:int = 124
print(f'Number {number} is ' + ('Even' if number % 2 == 0 else 'Odd'))
print("\n--------------------------------------------------------------------------------")

# Constants
from typing import Final

MY_CONST: Final[float] = 3.14
print(MY_CONST)
print("\n--------------------------------------------------------------------------------")


some_numbers: list[int] = [12, 34, 56, 78]
sum: int = 0
for i in some_numbers:
    sum += i
print("Sum of", some_numbers, "=", sum)
print("\n--------------------------------------------------------------------------------")

some_names: list[str] = ["Beat", "Christoph", "Adi", 'Single', "Double"]

print("Uppercase names:")
for name in some_names:
    print("-", name.upper())
print("--------------------")

some_names.sort()
print("Sorted names:", some_names)
print("--------------------")

short_names: list[str] = []
for name in some_names:
    if len(name) <= 4:
        short_names.append(name)
print("Short names: (append to list)", short_names)
print("--------------------")

short_names_comp: list[str] = [name for name in some_names if len(name) <= 4]
print("Short names: (comprehension)", short_names_comp)
print("\n--------------------------------------------------------------------------------")
