'''
Fünfstellige Zahl:
Bestimme eine fünfstellige Zahl, die 45-mal so gross ist wie das Produkt ihrer Ziffern.

Number of solutions: 1
1.Solution: {'a': 7, 'b': 7, 'c': 1, 'd': 7, 'e': 5} - Check: 77175
'''

from time import *
from constraint import *


def define_problem():
    problem = Problem()
    problem.addVariable("a", range(1, 10))
    problem.addVariable("b", range(10))
    problem.addVariable("c", range(10))
    problem.addVariable("d", range(10))
    problem.addVariable("e", range(10))

    problem.addConstraint(lambda a, b, c, d, e:
                          45 * a * b * c * d * e == 10000 * a + 1000 * b + 100 * c + 10 * d + e,
                          ["a", "b", "c", "d", "e"])
    return problem


def main():
    p: Problem = define_problem()
    solutions: list[dict] = p.getSolutions()
    print(f'Number of solutions: {len(solutions)}')
    for i, sol in enumerate(solutions, start=1):
        print(f'{i}.Solution: {sol} - Check: {45 * sol.get("a") * sol.get("b") * sol.get("c") * sol.get("d") * sol.get("e")}')


if __name__ == "__main__":
    time_start: float = time()
    main()
    time_end: float = time()
    print(f'Execution time: {round(time_end - time_start, 3)}')
