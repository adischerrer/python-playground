from enum import Enum

class State(Enum):
    """Represents the state of a node during DFS."""
    UNVISITED = 1
    VISITING = 2
    VISITED = 3

class CyclePathFinder:
    """Detects and returns the cycle path in a directed graph."""

    def __init__(self):
        self.adj = {}
        self.node_states = {}

    def _build_adjacency_list(self, relations: list[list[str]]):
        """Converts source-target relations into a graph adjacency list."""
        self.adj = {}
        self.node_states = {}
        all_nodes = set()

        for source, target in relations:
            all_nodes.add(source)
            all_nodes.add(target)

            if source not in self.adj:
                self.adj[source] = []
            self.adj[source].append(target)

        for node in all_nodes:
            self.adj.setdefault(node, [])
            self.node_states[node] = State.UNVISITED

    def _dfs(self, u: str, current_path: list[str]) -> list[str] | None:
        """
        Recursive DFS function modified to return the cycle path.

        :param u: The current node being visited.
        :param current_path: The list of nodes from the start node to u (the recursion stack).
        :return: A list of strings representing the cycle path (e.g., [A, B, C, A]),
                 or None if no cycle is found from this path.
        """
        # 1. Update state and path
        self.node_states[u] = State.VISITING
        current_path.append(u)

        # 2. Traverse neighbors (v)
        for v in self.adj.get(u, []):
            v_state = self.node_states.get(v)

            if v_state == State.VISITING:
                # Cycle found! 'v' is an ancestor of 'u' on the current path.

                # Find the index of the ancestor 'v' in the current_path
                try:
                    start_index = current_path.index(v)
                except ValueError:
                    # This should not happen if logic is correct, but for safety
                    return None

                    # The cycle path starts at 'v' and goes to 'u', then back to 'v'.
                # We return the sublist from 'v' onwards, and include 'v' again
                # to close the loop (u -> v is the back-edge).
                cycle = current_path[start_index:] + [v]
                return cycle

            if v_state == State.UNVISITED:
                # Continue DFS on unvisited neighbor
                cycle = self._dfs(v, current_path)
                if cycle is not None:
                    return cycle  # Cycle found deeper in the recursion

        # 3. Backtrack: remove u from the current path and mark as VISITED
        current_path.pop()
        self.node_states[u] = State.VISITED

        return None # No cycle found from this path

    def find_cycle(self, relations: list[list[str]]) -> list[str] | None:
        """
        Checks for a loop and returns the path if one is found.

        :param relations: A list of [source, target] pairs.
        :return: A list representing the first cycle found, or None.
        """
        self._build_adjacency_list(relations)

        for node in self.adj.keys():
            if self.node_states[node] == State.UNVISITED:
                # current_path tracks the nodes from the initial DFS call down to the current node
                cycle = self._dfs(node, [])
                if cycle is not None:
                    return cycle

        return None # No cycle found in the entire graph