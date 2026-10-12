# https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
Cheapest Flights Within K Stops

There are n cities connected by some flights. flights[i] = [from_i, to_i,
price_i] indicates a flight from city from_i to city to_i with cost
price_i. Given src, dst, and k, return the cheapest price from src to
dst with at most k stops (i.e. at most k+1 edges). If no such route
exists, return -1.

n is NOT redundant with flights, even though every city mentioned in
flights could be collected into a set: a city can legitimately have
zero flights in or out of it (still a valid city within [0, n-1]),
and the dist array must have a slot for every city 0..n-1 to safely
answer queries involving it (returning -1 if unreachable).

Approach: Bellman-Ford, capped at k+1 rounds (instead of the usual
N-1 rounds used for globally-shortest paths) since we specifically
want shortest paths using at most k+1 edges, not the overall
shortest path regardless of hop count.
1. dist = [inf] * n, except dist[src] = 0.
2. Repeat k+1 times:
   - Snapshot the current dist array (copy it) - relaxation in this
     round must read from the START-of-round state, not values
     already updated earlier in the SAME round. Otherwise two edges
     could get chained together within a single round, effectively
     allowing more than one additional hop per round and violating
     the k-stops cap.
   - For every edge (u, v, w) in flights: if snapshot[u] + w <
     dist[v], update dist[v] = snapshot[u] + w.
3. If dist[dst] is still inf, return -1; otherwise return dist[dst].

(Bellman-Ford's general/unconstrained form uses N-1 rounds instead of
k+1, guaranteed to converge since any shortest path - absent a
negative cycle - visits at most N-1 edges. An optional Nth round can
then detect negative cycles: if any edge can still be relaxed after
the guaranteed-stable N-1 rounds, a negative cycle is reachable from
src. Not needed here since costs are non-negative and we cap at k+1
rounds by problem design, not for cycle detection.)

Complexity Analysis:
--------------------
Time:  O(E * K), where E = len(flights), K = k+1 rounds. Each round
       relaxes every edge once.
Space: O(N) - two dist arrays of length n (current + the round's
       snapshot) alive at any one time; old snapshots are discarded
       each round, not accumulated.
"""

import copy


def solve(n, flights, src, dst, k):
    dist = [float("inf")] * n
    dist[src] = 0

    for _ in range(k + 1):
        snapshot = copy.deepcopy(dist)
        for u, v, w in flights:
            if snapshot[u] + w < dist[v]:
                dist[v] = snapshot[u] + w

    return dist[dst] if dist[dst] != float("inf") else -1


if __name__ == "__main__":
    n1 = 4
    flights1 = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert solve(n1, flights1, 0, 3, 1) == 700
    assert solve(n1, flights1, 0, 3, 0) == -1

    n3 = 3
    flights3 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert solve(n3, flights3, 0, 2, 1) == 200
    assert solve(n3, flights3, 0, 2, 0) == 500

    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(n, flights, src, dst, k):
        """Independent reference: DFS over all paths with at most k+1
        edges, tracking cost, no shared code with Bellman-Ford."""
        adj = {}
        for u, v, w in flights:
            adj.setdefault(u, []).append((v, w))

        best = [float("inf")]

        def dfs(node, cost, edges_used):
            if cost >= best[0]:
                return
            if node == dst:
                best[0] = min(best[0], cost)
                return
            if edges_used > k:
                return
            for nxt, w in adj.get(node, []):
                dfs(nxt, cost + w, edges_used + 1)

        dfs(src, 0, 0)
        return best[0] if best[0] != float("inf") else -1

    def random_graph(n, edge_count):
        flights = []
        seen = set()
        attempts = 0
        while len(flights) < edge_count and attempts < edge_count * 10:
            attempts += 1
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u == v or (u, v) in seen:
                continue
            seen.add((u, v))
            w = random.randint(1, 50)
            flights.append([u, v, w])
        return flights

    random.seed(42)
    trials = 300
    for t in range(trials):
        n = random.randint(2, 8)
        edge_count = random.randint(1, n * (n - 1) // 2)
        flights = random_graph(n, edge_count)
        src = random.randint(0, n - 1)
        dst = random.randint(0, n - 1)
        k = random.randint(0, n)

        expected = brute_force(n, flights, src, dst, k)
        actual = solve(n, flights, src, dst, k)

        assert expected == actual, (
            f"mismatch on trial {t}: n={n}, flights={flights}, src={src}, "
            f"dst={dst}, k={k}\nexpected={expected}, actual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
