# https://leetcode.com/problems/min-cost-to-connect-all-points/
"""
Min Cost to Connect All Points

You're given points[i] = [xi, yi]. The cost to connect any two points
i and j is their Manhattan distance: |xi - xj| + |yi - yj|. Any two
points can potentially be directly connected. Return the minimum
total cost to connect all points into a single network (a spanning
tree over all N points).

Approach: Kruskal's algorithm (Minimum Spanning Tree).
1. Generate every pairwise edge (N*(N-1)/2 of them) with its
   Manhattan-distance cost. Points are identified by their index
   into the input list (no need for named variables - UnionFind
   accepts any hashable element).
2. Sort edges by cost ascending.
3. Walk edges in sorted order; for each edge, if its two endpoints
   are NOT already connected (via Union-Find's find), union them and
   add the edge's cost to the running total. If they're already
   connected, skip it (adding it would create a cycle - wasted
   cost). Since edges are processed in ascending order, whichever
   edge first connects two components is guaranteed to be the
   cheapest possible edge available at that point - no need to
   compare costs manually.
4. By the time all edges are processed, exactly N-1 unions will have
   succeeded (one per connected pair of components), giving a full
   spanning tree.

Note: union() is used here purely for plain connectivity (no weight
argument) - the cost itself is accumulated separately in
total_cost. Passing the Manhattan-distance cost into union()'s
weight parameter would be a semantic mismatch (that parameter means
a division ratio x/y, used for problems like Evaluate Division, and
can even crash on a cost of 0 since it's used as a divisor there).

Complexity Analysis:
--------------------
Time:  O(N^2 log N), where N = number of points.
       - Generating edges: O(N^2) edges, O(1) cost each -> O(N^2).
       - Sorting: O(E log E) with E = O(N^2) edges, which substitutes
         to O(N^2 log(N^2)) = O(N^2 * 2 log N) = O(N^2 log N).
       - The Kruskal loop itself: O(N^2) edges processed, each with
         ~O(a(N)) (amortized near O(1)) find/union calls -> O(N^2).
       Sorting dominates, so overall O(N^2 log N).
Space: O(N^2) for the edges list (N*(N-1)/2 tuples), dominating the
       UnionFind's O(N) internal dict.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from union_find import UnionFind  # noqa: E402


def solve(points):
    elements = list(range(len(points)))

    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edges.append((cost, i, j))

    edges.sort()

    uf = UnionFind(elements)

    total_cost = 0
    for cost, i, j in edges:
        if uf.find(i) == uf.find(j):
            continue
        uf.union(i, j)
        total_cost += cost

    return total_cost


if __name__ == "__main__":
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    points2 = [[3, 12], [-2, 5], [-4, 1]]

    assert solve(points1) == 20
    assert solve(points2) == 18
    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(points):
        """Independent reference: generates its own edge list and
        runs its own from-scratch Union-Find (plain parent-pointer
        array, no path compression/union-by-size, no code shared
        with the main union_find module at all)."""
        n = len(points)
        if n <= 1:
            return 0

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                edges.append((cost, i, j))
        edges.sort()

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        total = 0
        count = 0
        for cost, i, j in edges:
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[ri] = rj
                total += cost
                count += 1
                if count == n - 1:
                    break
        return total

    def random_points(n, coord_range=20):
        return [
            [
                random.randint(-coord_range, coord_range),
                random.randint(-coord_range, coord_range),
            ]
            for _ in range(n)
        ]

    random.seed(42)
    trials = 300
    for t in range(trials):
        n = random.randint(1, 15)
        points = random_points(n)

        expected = brute_force(points)
        actual = solve(points)

        assert expected == actual, (
            f"mismatch on trial {t}: points={points}\n"
            f"expected={expected}, actual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
