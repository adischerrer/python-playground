# See https://www.youtube.com/watch?v=bD05uGo_sVI

from typing import Generator

def generate_numbers(limit: int) -> Generator:
    for i in range(0, limit):
        yield i

numbers: Generator = generate_numbers(limit=10)
# Get one element from the generator
print(next(numbers))
print(next(numbers))
print(next(numbers))
# Get the rest
print(list(numbers))