from datetime import date
from typing import Self


# __xyz__ Methods are called dunder (double underscore) methods.
# Here's an example to initialize (__init__) or represent (__repr__) an object

class Person:
    def __init__(self, name: str, birthday: date, email: str) -> None:
        self.name = name
        self.birthday = birthday
        self.email = email

    def __repr__(self) -> str:
        return f'Person(name={self.name}, birthday={self.birthday})'

    def age_in_days(self) -> int:
        return (date.today() - self.birthday).days

    def age_diff(self, other_person: Self) -> int:
        return abs((self.birthday - other_person.birthday).days)


adi: Person = Person('Adi', date(year=1970, month=3, day=3), 'adi.scherrer@gmail.com')
yvonne: Person = Person('Yvonne', date(year=1970, month=4, day=13), 'adi.scherrer@gmail.com')
print(adi)
print(yvonne)
print(f"{adi.name}'s age is {adi.age_in_days()} days")
print(f"{yvonne.name}'s age is {yvonne.age_in_days()} days")
print(f"Age difference between {yvonne.name} and {adi.name} is {adi.age_diff(yvonne)} days")
print("\n--------------------------------------------------------------------------------")

# Class info
print(f'{dir(Person)=}')
print(f'{adi.__dict__=}')
print(f'{adi.__dict__.keys()=}')
print(f'{adi.__dict__.values()=}')
print("\n--------------------------------------------------------------------------------")


# -----------------------------------------------------------------------------

# Returning "self" will allow method chaining
class Calc:
    def __init__(self, value: int = 0):
        self.value = value

    def increment(self, amount: int):
        self.value += amount
        return self  # Return self to allow chaining

    def multiply(self, factor: int):
        self.value *= factor
        return self  # Return self to allow chaining


print(f'{Calc(0).increment(5).multiply(3).value=}')
print(f'{Calc(-2).multiply(3).increment(12).multiply(6).value=}')
