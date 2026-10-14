# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
"""
Find the City With the Smallest Number of Neighbors at a Threshold
Distance

There are n cities numbered 0 to n-1. edges[i] = [from_i, to_i,
weight_i] represents a bidirectional (undirected) weighted road
between from_i and to_i. Given distanceThreshold, find the city that
has the SMALLEST number of other cities reachable within a total
path distance of at most distanceThreshold. If there's a tie, return
the city with the LARGEST index.

Approach: Floyd-Warshall (all-pairs shortest path).
1. The input is a sparse edge list, NOT a full distance grid - build
   an n x n dist matrix first: dist[i][i] = 0, dist[i][j] = edge
   weight for a direct road, else inf. Roads are undirected, so set
   both dist[u][v] and dist[v][u].
2. Relax over every possible intermediate node k (outermost loop),
   trying every (i, j) pair: dist[i][j] = min(dist[i][j],
   dist[i][k] + dist[k][j]). This triple loop must run to completion
   for ALL k before dist is trustworthy - counting/comparing cities
   using a partially-relaxed dist (e.g. mid-way through the k loop)
   gives wrong answers, since shorter paths via later k values
   haven't been discovered yet.
3. Only AFTER the full relax loop finishes: for each city i, count
   how many OTHER cities j (j != i) have dist[i][j] <=
   distanceThreshold. Track the minimum count, breaking ties toward
   the larger city index. This counting/tie-break step is a
   separate, sequential loop - not nested inside the relax loop.

Floyd-Warshall vs Dijkstra: Dijkstra computes shortest paths from
ONE single source; Floyd-Warshall computes shortest paths between
EVERY pair of nodes simultaneously (all-pairs) - a difference in
problem scope, not just algorithmic style. This also means
Floyd-Warshall doesn't "greedily finalize" a node's distance the way
Dijkstra does - dist[i][j] starts as just the direct edge weight (or
inf) and is only discovered to be shorter via some intermediate k as
the triple loop progresses.

Complexity Analysis:
--------------------
Time:  O(N^3) - dist matrix init is O(N^2), building it from edges is
       O(E), the triple-nested relax loop is O(N^3), and the final
       counting loop is O(N^2). The O(N^3) relax loop dominates.
Space: O(N^2) for the dist matrix.
"""


def solve(n, edges, distanceThreshold):
    dist = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for i, j, w in edges:
        dist[i][j] = w
        dist[j][i] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_distance = float("inf")
    min_distance_index = -1
    for i in range(n):
        cur_distance = 0
        for j in range(n):
            if j == i:
                continue
            if dist[i][j] <= distanceThreshold:
                cur_distance += 1
        if (cur_distance < min_distance) or (
            cur_distance == min_distance and i > min_distance_index
        ):
            min_distance = cur_distance
            min_distance_index = i

    return min_distance_index


if __name__ == "__main__":
    n1 = 4
    edges1 = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    assert solve(n1, edges1, 4) == 3

    n2 = 5
    edges2 = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    assert solve(n2, edges2, 2) == 0

    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(n, edges, distanceThreshold):
        """Independent reference: runs its own from-scratch Dijkstra
        per source node, no shared code with Floyd-Warshall."""
        import heapq

        adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def dijkstra(src):
            dist = [float("inf")] * n
            dist[src] = 0
            heap = [(0, src)]
            visited = set()
            while heap:
                d, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nxt, w in adj[node]:
                    nd = d + w
                    if nd < dist[nxt]:
                        dist[nxt] = nd
                        heapq.heappush(heap, (nd, nxt))
            return dist

        best_city = -1
        best_count = float("inf")
        for i in range(n):
            dist = dijkstra(i)
            count = sum(
                1 for j in range(n) if j != i and dist[j] <= distanceThreshold
            )
            if count <= best_count:
                best_count = count
                best_city = i
        return best_city

    def random_graph(n, edge_count, max_weight=20):
        edges = []
        seen = set()
        attempts = 0
        while len(edges) < edge_count and attempts < edge_count * 10:
            attempts += 1
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u == v or (u, v) in seen or (v, u) in seen:
                continue
            seen.add((u, v))
            w = random.randint(1, max_weight)
            edges.append([u, v, w])
        return edges

    random.seed(42)
    trials = 300
    for t in range(trials):
        n = random.randint(2, 8)
        max_edges = n * (n - 1) // 2
        edge_count = random.randint(1, max_edges)
        edges = random_graph(n, edge_count)
        distanceThreshold = random.randint(1, 60)

        expected = brute_force(n, edges, distanceThreshold)
        actual = solve(n, edges, distanceThreshold)

        assert expected == actual, (
            f"mismatch on trial {t}: n={n}, edges={edges}, "
            f"distanceThreshold={distanceThreshold}\n"
            f"expected={expected}, actual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
