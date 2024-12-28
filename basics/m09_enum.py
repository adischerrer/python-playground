from dataclasses import dataclass
from enum import Enum


class Color(Enum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"


@dataclass
class Car:
    brand: str
    color: Color


def main() -> None:
    c1: Car = Car(brand="BMW", color=Color.BLUE)
    c2: Car = Car(brand="Mercedes", color=Color.RED)
    c3: Car = Car(brand="Volvo", color=Color.GREEN)
    c4: Car = Car(brand="Mazda", color=Color.RED)
    c5: Car = Car(brand="VW", color=Color.GREEN)

    cars: list[Car] = [c1, c2, c3, c4, c5]
    print('All cars:')
    for car in cars:
        print(f'- {car=}')

    print('RED cars:')
    for car in cars:
        if car.color == Color.RED:
            print(f'- {car=}')


if __name__ == '__main__':
    main()
