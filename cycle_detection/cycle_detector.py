from enum import Enum

# Define the states for DFS cycle detection
class State(Enum):
    """Represents the state of a node during DFS."""
    UNVISITED = 1  # Not yet processed
    VISITING = 2   # Currently in the recursion stack (on the path)
    VISITED = 3    # Finished processing (no cycle found below it)

class CycleDetector:
    """Detects cycles in a directed graph represented by source-target relations."""

    def __init__(self):
        self.adj = {}
        self.node_states = {}

    def _build_adjacency_list(self, relations: list[list[str]]):
        """Converts source-target relations into a graph adjacency list."""
        self.adj = {}
        all_nodes = set()

        for source, target in relations:
            all_nodes.add(source)
            all_nodes.add(target)

            # Ensure source has an entry and add the edge
            if source not in self.adj:
                self.adj[source] = []
            self.adj[source].append(target)

        # Ensure all nodes (even those with no outgoing edges) are initialized
        for node in all_nodes:
            self.adj.setdefault(node, [])
            self.node_states[node] = State.UNVISITED

    def _dfs(self, u: str) -> bool:
        """
        Recursive Depth First Search to detect cycles.
        A cycle exists if we encounter a node that is currently VISITING.
        """
        # 1. Set current node to VISITING
        self.node_states[u] = State.VISITING

        # 2. Traverse neighbors (v)
        for v in self.adj.get(u, []):
            v_state = self.node_states.get(v)

            if v_state == State.VISITING:
                # Cycle found: A back-edge to a node on the current path
                return True

            if v_state == State.UNVISITED:
                # Continue DFS on unvisited neighbor
                if self._dfs(v):
                    return True  # Cycle found deeper in the recursion

        # 3. Current node and all its descendants have been processed
        self.node_states[u] = State.VISITED
        return False

    def has_loop(self, relations: list[list[str]]) -> bool:
        """
        Main function to check for a loop in the relations table.

        :param relations: A list of [source, target] pairs.
        :return: True if a loop (cycle) is found, False otherwise.
        """
        # 1. Build the graph and initialize states
        self._build_adjacency_list(relations)

        # 2. Perform DFS on every unvisited node (handles disconnected graphs)
        for node in self.adj.keys():
            if self.node_states[node] == State.UNVISITED:
                if self._dfs(node):
                    return True # Cycle found

        return False # No cycle found