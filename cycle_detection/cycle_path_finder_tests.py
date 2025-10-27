from cycle_detection.cycle_path_finder import CyclePathFinder

pathFinder = CyclePathFinder()

# Example 1: Simple cycle A -> B -> C -> A
relations1 = [
    ["A", "B"],
    ["B", "C"],
    ["C", "A"],
    ["X", "Y"] # Disconnected component
]
print(f"Cycle 1 (A->B->C->A): {pathFinder.find_cycle(relations1)}")
# Expected output: ['A', 'B', 'C', 'A']

# Example 2: Longer cycle with intermediate nodes
relations2 = [
    ["S", "T"],
    ["T", "U"],
    ["U", "V"],
    ["V", "T"] # Back-edge V -> T
]
print(f"Cycle 2 (T->U->V->T): {pathFinder.find_cycle(relations2)}")
# Expected output: ['T', 'U', 'V', 'T']
# Note: The path starts at 'S' but the cycle only includes T, U, V.

# Example 3: No cycle
relations3 = [
    ["P", "Q"],
    ["Q", "R"],
    ["R", "S"],
    ["S", "T"]
]
print(f"Cycle 3 (No loop): {pathFinder.find_cycle(relations3)}")
# Expected output: None

# Example 4: Disconnected graph with a cycle
relations4 = [
    ["1", "2"],
    ["A", "B"],
    ["B", "C"],
    ["C", "A"] # Cycle: A -> B -> C -> A
]
print(f"Cycle 4 (A->B->C->A): {pathFinder.find_cycle(relations4)}")
# Expected output: ['A', 'B', 'C', 'A'] (or ['1', '2'] if a cycle existed there)