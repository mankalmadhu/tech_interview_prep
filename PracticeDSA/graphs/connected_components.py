from collections import deque


def connected_components(graph):
    """
    Calculates the number of connected components in an undirected graph.

      Strategy:
      1. Maintain a global `visited` set to track all nodes processed so far.
      2. Iterate through every node in the graph (keys of the adjacency dict).
      3. If a node has NOT been visited yet, it implies the discovery of a new
         unconnected component.
         - Increment the component count.
         - Trigger a traversal (BFS/DFS) to find and mark ALL nodes reachable
           from this node as visited.

      Complexity Analysis:
      --------------------
      Time Complexity: O(V + E)
          - O(V): We iterate through every vertex exactly once in the main loop
            to check if it's visited.
          - O(E): During the traversals (summed up), we iterate over every edge
            exactly twice (once from each end).

      Space Complexity: O(V)
          - O(V): To store the `visited` set containing all vertices.
          - O(V): Auxiliary space for the BFS Queue (or DFS Stack) in the
            worst-case scenario.

      Example Run-Through:
      --------------------
      Graph: {0: [1], 1: [0], 2: []}
      (Node 0 connected to 1. Node 2 is isolated).

      1. Init: visited = set(), count = 0

      2. Loop node 0:
         - 0 is NOT in visited.
         - Increment count -> 1.
         - Call BFS(0):
           - Queue adds 0. Visited adds 0.
           - Pop 0. Neighbors: [1].
           - 1 not visited. Queue adds 1. Visited adds 1.
           - Pop 1. Neighbors: [0]. 0 already visited.
           - Queue empty. BFS ends.
         - Current state: visited = {0, 1}

      3. Loop node 1:
         - 1 IS in visited.
         - Continue (Skip).

      4. Loop node 2:
         - 2 is NOT in visited.
         - Increment count -> 2.
         - Call BFS(2):
           - Queue adds 2. Visited adds 2.
           - Pop 2. Neighbors: [].
           - Queue empty. BFS ends.
         - Current state: visited = {0, 1, 2}

      5. Loop Ends. Return count (2).
    """
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            count += 1
            visited.add(node)
            __bfs(graph, node, visited)

    return count


def __bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        cur_node = queue.popleft()
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def _brute_force_components(graph):
    """Independent check via union-find over the same adjacency dict."""
    parent = {node: node for node in graph}

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            union(node, neighbor)

    return len({find(node) for node in graph})


if __name__ == "__main__":
    print(connected_components({0: [1], 1: [0], 2: []}))  # expect 2
    print(connected_components({0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}))  # expect 2
    print(connected_components({0: [], 1: [], 2: [], 3: []}))  # expect 4

    import random

    for trial in range(300):
        n = random.randint(1, 20)
        possible_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
        random.shuffle(possible_edges)
        num_edges = random.randint(0, len(possible_edges))
        chosen = possible_edges[:num_edges]

        graph = {i: [] for i in range(n)}
        for u, v in chosen:
            graph[u].append(v)
            graph[v].append(u)

        got = connected_components(graph)
        expected = _brute_force_components(graph)
        assert got == expected, f"Mismatch n={n}, graph={graph}: got {got}, expected {expected}"

    print("All stress tests passed!")
