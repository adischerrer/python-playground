from collections import Counter
from turtledemo.penrose import start

letters: list[str] = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd']
print(f'{letters=}')
print("\n--------------------------------------------------------------------------------")

counter: Counter = Counter(letters)
print(f'{counter.total()=}')
print(f'{counter.most_common()=}')
print(f'{counter.most_common(n=2)=}')

# Enumerate normally is zero based
for i, letter in enumerate(letters):
    print(f'{i} : {letter}')
print("\n--------------------------------------------------------------------------------")

# Start value can be defined optionally
for i, letter in enumerate('This is a text', start=1):
    print(f'{i} : {letter}')
print("\n--------------------------------------------------------------------------------")
