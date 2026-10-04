"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/graphs/dfs.py until you're done.

Problem (Depth-First Search on a Graph):

Given a graph represented as an adjacency list (dict: node -> list of
neighbors) and a starting node, return the list of nodes in the order
they are visited by a DFS traversal.

Example:
  graph = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A', 'D'],
      'D': ['B', 'C'],
  }
  start = 'A'
  output = ['A', 'B', 'D', 'C']  (one valid DFS order)

Write your solution below.
"""


def dfs(graph, start):
    visited = set()
    result = []
    return _dfs_rec(graph, start,visited, result)

def _dfs_rec(graph, node, visited, result):
    visited.add(node)
    result.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            _dfs_rec(graph, neighbor, visited, result)

    return result

def dfs_it(graph, start):
    visited = set([start])
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)

    return result



if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    print(dfs(graph, "A"))
    print(dfs_it(graph, "A"))  # expect ['A', 'B', 'D', 'C']

    assert dfs(graph, "A") == ["A", "B", "D", "C"]
    assert dfs_it(graph, "A") == ["A", "B", "D", "C"]
    assert dfs({"A": []}, "A") == ["A"]
    assert dfs_it({"A": []}, "A") == ["A"]
    chain = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert dfs(chain, "A") == ["A", "B", "C"]
    assert dfs_it(chain, "A") == ["A", "B", "C"]
    print("fixed cases passed")

    import random

    def build_random_graph(n, extra_edges):
        nodes = list(range(n))
        g = {i: [] for i in nodes}
        for i in range(1, n):
            parent = random.randint(0, i - 1)
            g[parent].append(i)
            g[i].append(parent)
        for _ in range(extra_edges):
            a, b = random.randint(0, n - 1), random.randint(0, n - 1)
            if a != b and b not in g[a]:
                g[a].append(b)
                g[b].append(a)
        return g

    for _ in range(300):
        n = random.randint(1, 12)
        g = build_random_graph(n, random.randint(0, n))
        got_rec = dfs(g, 0)
        got_it = dfs_it(g, 0)
        # both must visit every reachable node exactly once; exact order can
        # legitimately differ when a node has multiple valid parents (e.g. a
        # diamond/cycle), since recursive marks-on-entry while iterative
        # marks-on-push -- see diamond example discussed above
        assert set(got_rec) == set(g.keys()), f"graph={g}: recursive missed nodes {got_rec}"
        assert len(got_rec) == len(set(got_rec)), f"graph={g}: recursive revisited a node {got_rec}"
        assert set(got_it) == set(g.keys()), f"graph={g}: iterative missed nodes {got_it}"
        assert len(got_it) == len(set(got_it)), f"graph={g}: iterative revisited a node {got_it}"
    print("300 randomized trials passed")
