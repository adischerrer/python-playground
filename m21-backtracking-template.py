# Found at https://gist.github.com/RuolinZheng08/cdd880ee748e27ed28e0be3916f56fa6

def is_valid_state(state):
    # check if it is a valid solution
    return True


def get_candidates(state):
    return []


def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions
