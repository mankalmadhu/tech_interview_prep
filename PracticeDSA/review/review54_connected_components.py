"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/graphs/connected_components.py until you're done.

Problem (Connected Components in an Undirected Graph):

Given an undirected graph with n nodes (labeled 0..n-1) and a list
of edges, return the number of connected components in the graph.

Example:
  n = 5
  edges = [[0, 1], [1, 2], [3, 4]]
  output = 2
  (components: {0,1,2} and {3,4})

Write your solution below.
"""
from collections import deque

def count_components(n, edges):
    adj_mat= {i: [] for i in range(n)}

    for u, v in edges:
        adj_mat[u].append(v)
        adj_mat[v].append(u)

    visited = set()
    connected_count = 0

    for node in adj_mat.keys():
        if node not in visited:
            visited.add(node)
            _bfs(adj_mat, node, visited)
            connected_count += 1

    return connected_count



def _bfs(graph, start, visited):

    q = deque([start])

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)



def brute_force_components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for u, v in edges:
        union(u, v)

    return len({find(i) for i in range(n)})


if __name__ == "__main__":
    print(count_components(5, [[0, 1], [1, 2], [3, 4]]))  # expect 2
    print(count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # expect 1
    print(count_components(4, []))  # expect 4

    import random

    for trial in range(300):
        n = random.randint(1, 20)
        possible_edges = [(u, v) for u in range(n) for v in range(u + 1, n)]
        random.shuffle(possible_edges)
        num_edges = random.randint(0, len(possible_edges))
        edges = possible_edges[:num_edges]
        # randomize u/v order within each edge to catch directional bugs
        edges = [[u, v] if random.random() < 0.5 else [v, u] for u, v in edges]
        random.shuffle(edges)

        got = count_components(n, edges)
        expected = brute_force_components(n, edges)
        assert got == expected, f"Mismatch n={n}, edges={edges}: got {got}, expected {expected}"

    print("All stress tests passed!")
