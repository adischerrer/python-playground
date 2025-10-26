from cycle_detection.cycle_detector import CycleDetector

detector = CycleDetector()

# Example 1: With a loop (A -> B -> C -> A)
relations1 = [
    ["A", "B"],
    ["B", "C"],
    ["C", "A"],
    ["D", "E"]
]
print(f"Has Loop 1 (Expected: True): {detector.has_loop(relations1)}")

# Example 2: Without a loop (A -> B -> C, D -> E)
relations2 = [
    ["A", "B"],
    ["B", "C"],
    ["D", "E"],
    ["E", "F"]
]
print(f"Has Loop 2 (Expected: False): {detector.has_loop(relations2)}")

# Example 3: Self-contained loop (Y -> Z -> Y)
relations3 = [
    ["X", "Y"],
    ["Y", "Z"],
    ["Z", "Y"]
]
print(f"Has Loop 3 (Expected: True): {detector.has_loop(relations3)}")

# Example 4: A single node self-loop (A -> A)
relations4 = [
    ["A", "A"]
]
print(f"Has Loop 4 (Expected: True): {detector.has_loop(relations4)}")