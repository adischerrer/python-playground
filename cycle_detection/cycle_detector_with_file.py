from cycle_detection.cycle_detector import CycleDetector

detector = CycleDetector()
relations = []

left: list[int] = []
right: list[int] = []

with open('input.txt', 'r') as file:
    for line in file:
        tokens: list[str] = line.split()
        relations.append([tokens[0], tokens[1]])

print(f"Has Loop: {detector.has_loop(relations)}")
