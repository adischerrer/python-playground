from cycle_detection.cycle_path_finder import CyclePathFinder

pathFinder = CyclePathFinder()
relations = []

left: list[int] = []
right: list[int] = []

with open('input.txt', 'r') as file:
    for line in file:
        tokens: list[str] = line.split()
        relations.append([tokens[0], tokens[1]])

print(f"Result: {pathFinder.find_cycle(relations)}")
