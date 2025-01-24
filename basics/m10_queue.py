# PriorityQueue form built-in library.
# Alternatively, a self-made class can be used (see https://www.geeksforgeeks.org/priority-queue-in-python/)

from queue import PriorityQueue

customers = PriorityQueue()
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))

while not customers.empty():
    print(customers.get()[1])
