from collections import deque


def bfs(graph, start):
    """
    Performs Breadth-First Search (BFS) on a graph.

    Strategy: Level-Order Traversal using a Queue
    ---------------------------------------------
    BFS explores the graph layer by layer, starting from the source.

    1. Data Structure: Queue (Deque).
       - Essential for maintaining the FIFO order required to process
         all neighbors of depth 'd' before any node at depth 'd+1'.
    2. Visited Set:
       - Keeps track of visited nodes to prevent cycles and redundant processing.

    Algorithm:
    - Push 'start' to queue and mark visited.
    - While queue is not empty:
      - Pop node from LEFT (oldest).
      - Add unvisited neighbors to RIGHT (newest) and mark them visited immediately.

    Complexity Analysis:
    --------------------
    Time Complexity: O(V + E)
       - We visit every Vertex (V) once.
       - We iterate over every Edge (E) associated with those vertices.

    Space Complexity: O(V)
       - To store the visited set and the queue (which can hold up to V nodes
         in the worst case, e.g., a star graph).
    """
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        cur_node = queue.popleft()
        result.append(cur_node)
        for neighbor in graph[cur_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }
    assert bfs(graph, "A") == ["A", "B", "C", "D"]
    assert bfs({"A": []}, "A") == ["A"]
    assert bfs({"A": ["B"], "B": ["A"]}, "A") == ["A", "B"]
    chain = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    assert bfs(chain, "A") == ["A", "B", "C"]
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

    def depth_map(order_list, g, start):
        depth = {start: 0}
        for node in order_list:
            for nb in g.get(node, []):
                if nb not in depth or depth[nb] > depth[node] + 1:
                    depth[nb] = depth[node] + 1
        return depth

    def true_bfs_depth(g, start):
        # independent re-derivation via explicit frontier levels (no queue)
        depth = {start: 0}
        frontier = [start]
        d = 0
        while frontier:
            next_frontier = []
            for node in frontier:
                for nb in g.get(node, []):
                    if nb not in depth:
                        depth[nb] = d + 1
                        next_frontier.append(nb)
            frontier = next_frontier
            d += 1
        return depth

    for _ in range(300):
        n = random.randint(1, 12)
        g = build_random_graph(n, random.randint(0, n))
        got = bfs(g, 0)
        assert set(got) == set(g.keys()), f"graph={g}: node coverage mismatch, got {got}"
        got_depth = depth_map(got, g, 0)
        want_depth = true_bfs_depth(g, 0)
        assert got_depth == want_depth, f"graph={g}: depth mismatch {got_depth} vs {want_depth}"
    print("300 randomized trials passed")
