# https://leetcode.com/problems/redundant-connection/
"""
Redundant Connection

You're given a graph that started as a tree with n nodes, but one
extra edge was added, creating exactly one cycle. `edges` is a list
of [u, v] pairs (1-indexed), given in the order they were added.
Return the edge that, if removed, turns the graph back into a tree.

Approach: process edges in order with Union-Find. For each edge
(u, v), check connected(u, v) *before* union-ing. If u and v are
already in the same component, this edge doesn't connect two
previously-separate parts of the tree - it's the one creating the
cycle, so return it immediately. The problem's guarantee (exactly
one extra edge beyond a valid tree) means only one edge can ever
trigger this condition, so there's no need to track candidates - the
first (and only) hit is the answer.

Complexity Analysis:
--------------------
Time:  O(N * a(N)) - N edges, each processed with one find/union
       pair at amortized O(a(N)) (effectively O(1) in practice).
       Simplifies to O(N).
Space: O(N) for the UnionFind's internal dict.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from union_find import UnionFind  # noqa: E402


def solve(edges):
    elements = list({x for sublist in edges for x in sublist})
    uf = UnionFind(elements)

    for edge in edges:
        if uf.find(edge[0]) == uf.find(edge[1]):
            return edge
        uf.union(edge[0], edge[1])


if __name__ == "__main__":
    assert solve([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert solve([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(edges):
        """Independent reference: incremental adjacency-list + BFS
        reachability check (no union-find reused at all). Processes
        edges in given order, returns the first edge whose two
        endpoints are already reachable from each other."""
        adj = {}

        def reachable(src, dst):
            if src not in adj:
                return False
            seen = {src}
            queue = [src]
            while queue:
                node = queue.pop()
                if node == dst:
                    return True
                for nxt in adj.get(node, []):
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            return False

        for u, v in edges:
            if reachable(u, v):
                return [u, v]
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        return None

    def random_tree_plus_one_edge(n):
        """Builds a random spanning tree over nodes 1..n (n-1 edges),
        then adds one extra edge between two existing, not-yet-
        directly-connected nodes, inserted at a random position."""
        edges = []
        for node in range(2, n + 1):
            parent = random.randint(1, node - 1)
            edges.append([parent, node])

        existing = {frozenset(e) for e in edges}
        while True:
            u, v = random.sample(range(1, n + 1), 2)
            if frozenset((u, v)) not in existing:
                break
        extra_edge = [u, v]

        pos = random.randint(0, len(edges))
        edges.insert(pos, extra_edge)
        return edges

    random.seed(42)
    trials = 300
    for t in range(trials):
        n = random.randint(3, 15)
        edges = random_tree_plus_one_edge(n)

        expected = brute_force(edges)
        actual = solve(edges)

        assert expected == actual, (
            f"mismatch on trial {t}: edges={edges}\n"
            f"expected={expected}, actual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
