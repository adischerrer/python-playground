'''
Zahlendreher:
In einer vierstelligen Zahl ändert man die Reihenfolge der Ziffern und
erhält die neue Zahl. Die Differenz der ursprünglichen und der neuen
Zahl ist wieder vierstellig und benutzt wieder die gleichen 4 Ziffern.

Number of solutions: 50
Solution 1: x=9954, y=4995, z=4959, (x-y==z)=True
Solution 2: x=9954, y=4959, z=4995, (x-y==z)=True
Solution 3: x=9864, y=4968, z=4896, (x-y==z)=True
Solution 4: x=9864, y=4896, z=4968, (x-y==z)=True
Solution 5: x=9774, y=4977, z=4797, (x-y==z)=True
Solution 6: x=9774, y=4797, z=4977, (x-y==z)=True
Solution 7: x=9684, y=4986, z=4698, (x-y==z)=True
Solution 8: x=9684, y=4698, z=4986, (x-y==z)=True
Solution 9: x=9612, y=6921, z=2691, (x-y==z)=True
Solution 10: x=9612, y=2691, z=6921, (x-y==z)=True
Solution 11: x=9594, y=4995, z=4599, (x-y==z)=True
Solution 12: x=9594, y=4599, z=4995, (x-y==z)=True
Solution 13: x=9540, y=4950, z=4590, (x-y==z)=True
Solution 14: x=9540, y=4590, z=4950, (x-y==z)=True
Solution 15: x=9504, y=5409, z=4095, (x-y==z)=True
Solution 16: x=9504, y=4095, z=5409, (x-y==z)=True
Solution 17: x=9324, y=4932, z=4392, (x-y==z)=True
Solution 18: x=9324, y=4392, z=4932, (x-y==z)=True
Solution 19: x=9180, y=8091, z=1089, (x-y==z)=True
Solution 20: x=9180, y=1089, z=8091, (x-y==z)=True
Solution 21: x=9108, y=8019, z=1089, (x-y==z)=True
Solution 22: x=9108, y=1089, z=8019, (x-y==z)=True
Solution 23: x=9045, y=4950, z=4095, (x-y==z)=True
Solution 24: x=9045, y=4095, z=4950, (x-y==z)=True
Solution 25: x=8523, y=5238, z=3285, (x-y==z)=True
Solution 26: x=8523, y=3285, z=5238, (x-y==z)=True
Solution 27: x=8235, y=5382, z=2853, (x-y==z)=True
Solution 28: x=8235, y=2853, z=5382, (x-y==z)=True
Solution 29: x=7641, y=6174, z=1467, (x-y==z)=True
Solution 30: x=7641, y=1467, z=6174, (x-y==z)=True
Solution 31: x=7614, y=6147, z=1467, (x-y==z)=True
Solution 32: x=7614, y=1467, z=6147, (x-y==z)=True
Solution 33: x=6417, y=4671, z=1746, (x-y==z)=True
Solution 34: x=6417, y=1746, z=4671, (x-y==z)=True
Solution 35: x=6147, y=4671, z=1476, (x-y==z)=True
Solution 36: x=6147, y=1476, z=4671, (x-y==z)=True
Solution 37: x=5823, y=3285, z=2538, (x-y==z)=True
Solution 38: x=5823, y=2538, z=3285, (x-y==z)=True
Solution 39: x=5238, y=2853, z=2385, (x-y==z)=True
Solution 40: x=5238, y=2385, z=2853, (x-y==z)=True
Solution 41: x=5031, y=3501, z=1530, (x-y==z)=True
Solution 42: x=5031, y=1530, z=3501, (x-y==z)=True
Solution 43: x=5022, y=2520, z=2502, (x-y==z)=True
Solution 44: x=5022, y=2502, z=2520, (x-y==z)=True
Solution 45: x=5013, y=3510, z=1503, (x-y==z)=True
Solution 46: x=5013, y=1503, z=3510, (x-y==z)=True
Solution 47: x=4932, y=2493, z=2439, (x-y==z)=True
Solution 48: x=4932, y=2439, z=2493, (x-y==z)=True
Solution 49: x=2961, y=1692, z=1269, (x-y==z)=True
Solution 50: x=2961, y=1269, z=1692, (x-y==z)=True
Execution time: 1034
'''

from time import *

from constraint import *


def print_solution(i: int, sol: dict[str, int]):
    x: int = sol.get("a1") * 1000 + sol.get("b1") * 100 + sol.get("c1") * 10 + sol.get("d1")
    y: int = sol.get("a2") * 1000 + sol.get("b2") * 100 + sol.get("c2") * 10 + sol.get("d2")
    z: int = sol.get("a3") * 1000 + sol.get("b3") * 100 + sol.get("c3") * 10 + sol.get("d3")
    print(f'Solution {i}: {x=}, {y=}, {z=}, {(x-y==z)=}')


def define_problem():
    p = Problem()
    p.addVariable("a1", range(1, 10))
    p.addVariable("b1", range(10))
    p.addVariable("c1", range(10))
    p.addVariable("d1", range(10))

    p.addVariable("a2", range(1, 10))
    p.addVariable("b2", range(10))
    p.addVariable("c2", range(10))
    p.addVariable("d2", range(10))

    p.addVariable("a3", range(1, 10))
    p.addVariable("b3", range(10))
    p.addVariable("c3", range(10))
    p.addVariable("d3", range(10))

    p.addConstraint(lambda a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3:
                    (a1 * 1000 + b1 * 100 + c1 * 10 + d1)
                    - (a2 * 1000 + b2 * 100 + c2 * 10 + d2)
                    == (a3 * 1000 + b3 * 100 + c3 * 10 + d3),
                    ["a1", "b1", "c1", "d1", "a2", "b2", "c2", "d2", "a3", "b3", "c3", "d3"])
    p.addConstraint(lambda a1, b1, c1, d1, a2, b2, c2, d2: sorted([a1, b1, c1, d1]) == sorted([a2, b2, c2, d2]),
                    ["a1", "b1", "c1", "d1", "a2", "b2", "c2", "d2"])
    p.addConstraint(lambda a1, b1, c1, d1, a3, b3, c3, d3: sorted([a1, b1, c1, d1]) == sorted([a3, b3, c3, d3]),
                    ["a1", "b1", "c1", "d1", "a3", "b3", "c3", "d3"])
    return p


def main():
    find_all_solutions: bool = False

    p: Problem = define_problem()
    if find_all_solutions:
        solutions: list[dict] = p.getSolutions()
        print(f'Number of solutions: {len(solutions)}')
        for i, sol in enumerate(solutions, start=1):
            print_solution(i, sol)
    else:
        sol: dict[str, int] = p.getSolution()
        print_solution(1, sol)


if __name__ == "__main__":
    print("Finding one solution takes about 60 sec. Finding all solutions takes much longer.")
    time_start: float = time()
    main()
    time_end: float = time()
    print(f'Execution time: {round(time_end - time_start)}')
