def dfs(graph, start_node):
    """
    Performs Depth-First Search (DFS) on a graph.

    Strategy: Recursive Traversal
    -----------------------------
    DFS explores as far as possible along each branch before backtracking.

    1. Visited Set:
       - Tracks nodes to prevent processing cycles or redundant visits.
    2. Recursion (Implicit Stack):
       - Instead of an explicit stack data structure, we rely on the
         Call Stack of the program to manage the backtracking order.

    Algorithm:
    - Mark current 'node' as visited and add to result.
    - For each neighbor:
      - If not visited, recursively call dfs on that neighbor.
      - This "pauses" the current node's loop until the neighbor returns.

    Complexity Analysis:
    --------------------
    Time Complexity: O(V + E)
       - We visit every Vertex (V) once.
       - We check every Edge (E) exactly twice (once from each end).

    Space Complexity: O(V)
       - Visited set stores O(V) nodes.
       - Recursion Stack depth can go up to O(V) in the worst case
         (e.g., a straight line graph).
    """
    visited = set()
    result = []
    __dfs_recursive(graph, start_node, visited, result)
    return result


def __dfs_recursive(graph, node, visited, result):
    visited.add(node)
    result.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            __dfs_recursive(graph, neighbor, visited, result)


def dfs_iterative(graph, start_node):
    """
    Iterative DFS using an explicit stack.

    Key subtlety vs the recursive version: nodes are marked visited at
    PUSH time here (not when popped/processed). This matters when a node
    has multiple valid "parents" (e.g. a diamond shape in the graph) -
    whichever node pushes it first "claims" it, which can differ from
    which node would have claimed it under the recursive version's
    mark-on-entry semantics. Both are valid DFS traversals (every node
    visited exactly once via a real edge), they just may disagree on
    which edge was used to first discover a shared descendant.

    We push neighbors in reversed() order so popping (LIFO) processes
    them in the same left-to-right order as the recursive version would
    for the *first* node's neighbors (though divergence can still occur
    deeper in the traversal on diamonds/cycles, as explained above).

    Time Complexity: O(V + E)
    Space Complexity: O(V) - visited set + stack, each up to O(V).
    """
    visited = set([start_node])
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return result


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    assert dfs(graph, "A") == ["A", "B", "D", "C"]
    assert dfs_iterative(graph, "A") == ["A", "B", "D", "C"]
    assert dfs({"A": []}, "A") == ["A"]
    assert dfs_iterative({"A": []}, "A") == ["A"]
    chain = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert dfs(chain, "A") == ["A", "B", "C"]
    assert dfs_iterative(chain, "A") == ["A", "B", "C"]
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
        got_it = dfs_iterative(g, 0)
        assert set(got_rec) == set(g.keys()), f"graph={g}: recursive missed nodes {got_rec}"
        assert len(got_rec) == len(set(got_rec)), f"graph={g}: recursive revisited a node"
        assert set(got_it) == set(g.keys()), f"graph={g}: iterative missed nodes {got_it}"
        assert len(got_it) == len(set(got_it)), f"graph={g}: iterative revisited a node"
    print("300 randomized trials passed")
