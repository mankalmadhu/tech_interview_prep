"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/graphs/bfs.py until you're done.

Problem (Breadth-First Search on a Graph):

Given a graph represented as an adjacency list (dict: node -> list of
neighbors) and a starting node, return the list of nodes in the order
they are visited by a BFS traversal.

Example:
  graph = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A', 'D'],
      'D': ['B', 'C'],
  }
  start = 'A'
  output = ['A', 'B', 'C', 'D']

Write your solution below.
"""
from collections import deque

def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    result = []

    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return result



if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    print(bfs(graph, "A"))  # expect ['A', 'B', 'C', 'D']

    assert bfs(graph, "A") == ["A", "B", "C", "D"]
    assert bfs({"A": []}, "A") == ["A"]
    assert bfs({"A": ["B"], "B": ["A"]}, "A") == ["A", "B"]
    # disconnected-looking from B's perspective shouldn't matter, start node drives traversal
    chain = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert bfs(chain, "A") == ["A", "B", "C"]
    print("fixed cases passed")

    import random

    def brute_force_levels(graph, start):
        # independent level-by-level re-derivation using a frontier set
        visited = {start}
        order = [start]
        frontier = [start]
        while frontier:
            next_frontier = []
            for node in frontier:
                for neighbor in sorted(graph.get(node, [])):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        order.append(neighbor)
                        next_frontier.append(neighbor)
            frontier = next_frontier
        return order

    def build_random_graph(n, extra_edges):
        nodes = list(range(n))
        graph = {i: [] for i in nodes}
        # connect as a random tree first to guarantee connectivity from node 0
        for i in range(1, n):
            parent = random.randint(0, i - 1)
            graph[parent].append(i)
            graph[i].append(parent)
        for _ in range(extra_edges):
            a, b = random.randint(0, n - 1), random.randint(0, n - 1)
            if a != b and b not in graph[a]:
                graph[a].append(b)
                graph[b].append(a)
        return graph

    for _ in range(300):
        n = random.randint(1, 12)
        graph = build_random_graph(n, random.randint(0, n))
        got = bfs(graph, 0)
        want_levels = brute_force_levels(graph, 0)
        # compare via level-depth, not exact tie order (neighbor iteration order may differ)
        def depth_map(order_list, g, start):
            depth = {start: 0}
            for node in order_list:
                for nb in g.get(node, []):
                    if nb not in depth or depth[nb] > depth[node] + 1:
                        depth[nb] = depth[node] + 1
            return depth
        assert set(got) == set(want_levels), f"graph={graph}: node set mismatch {got} vs {want_levels}"
        got_depth = depth_map(got, graph, 0)
        want_depth = depth_map(want_levels, graph, 0)
        assert got_depth == want_depth, f"graph={graph}: depth mismatch {got_depth} vs {want_depth}"
    print("300 randomized trials passed")
