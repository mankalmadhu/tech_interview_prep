# https://leetcode.com/problems/evaluate-division/
"""
Evaluate Division

You're given equations[i] = [A, B] and values[i] = v, meaning
A / B = v. Given queries[i] = [C, D], return C / D for each query,
computed by chaining known equations (e.g. a/b=2, b/c=3 => a/c=6).
If C or D doesn't appear in any equation, or there's no path
connecting them, return -1.0 for that query.

Approach: weighted Union-Find (the shared UnionFind class was
extended this session to carry a weight alongside each node's
parent pointer: parent_lookup[x] = (parent, size, weight), where
weight == x / parent). union(x, y, value) finds both roots + x's
and y's weights relative to their roots (via the find_with_weight
path-compression climb), then attaches one root under the other
with a weight computed so the x/y = value relationship holds
through the roots. find/get_node_weight expose the root and the
accumulated weight-to-root for any node.

Complexity Analysis:
--------------------
Time:  O(E + Q), where E = number of equations, Q = number of
       queries.
       - Building unique_entries and the UnionFind init are each
         O(N) (N = unique variable count, N <= 2E).
       - The union loop does E unions, each ~O(a(N)) (amortized
         near O(1)) thanks to path compression + union by size.
       - The query loop does Q lookups, each ~O(a(N)).
       So overall O(E + Q) (the inverse-Ackermann factor is dropped
       as effectively constant).
Space: O(N) for the UnionFind's internal dict, O(Q) for the output
       list.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from union_find import UnionFind  # noqa: E402


def solve(equations, values, queries):
    unique_entries = list({var for eq in equations for var in eq})
    uf = UnionFind(unique_entries)

    for i in range(len(equations)):
        uf.union(equations[i][0], equations[i][1], values[i])

    result = []
    for query in queries:
        q1, q2 = query
        r1 = uf.find(q1)
        r2 = uf.find(q2)

        if r1 is None or r2 is None:
            result.append(-1.0)
            continue

        if r1 != r2:
            result.append(-1.0)
        else:
            result.append(uf.get_node_weight(q1) / uf.get_node_weight(q2))

    return result


if __name__ == "__main__":
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected1 = [6.0, 0.5, -1.0, 1.0, -1.0]

    result1 = solve(equations1, values1, queries1)
    for got, want in zip(result1, expected1):
        assert (got == -1.0 and want == -1.0) or abs(got - want) < 1e-6, (
            f"mismatch: got={result1}, want={expected1}"
        )
    print("Example test passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(equations, values, queries):
        """Independent reference: builds its own weighted adjacency
        graph (two directed edges per equation: A->B with value,
        B->A with 1/value), then DFS's from C to D for each query,
        multiplying edge weights along the path. No union-find
        reused at all."""
        graph = {}
        for (a, b), v in zip(equations, values):
            graph.setdefault(a, {})[b] = v
            graph.setdefault(b, {})[a] = 1.0 / v

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for nxt, w in graph[src].items():
                if nxt in visited:
                    continue
                sub = dfs(nxt, dst, visited)
                if sub != -1.0:
                    return w * sub
            return -1.0

        answers = []
        for c, d in queries:
            answers.append(dfs(c, d, set()))
        return answers

    def random_equations_and_queries(num_vars, num_equations, num_queries):
        """Generates num_vars distinct variable names, connects a
        random spanning-tree-like chain of equations among a random
        subset of them (so some variables may be isolated/unused -
        on purpose, to exercise the -1.0 cases), then adds a few
        extra equations for redundancy (using the ratio already
        implied by the existing chain, so the graph stays
        consistent - a randomly chosen value could otherwise create
        a conflicting cycle with no valid real-world equivalent),
        and finally random queries (some answerable, some not)."""
        variables = [f"v{i}" for i in range(num_vars)]
        used = random.sample(variables, k=random.randint(1, num_vars))

        equations = []
        values = []
        for i in range(1, len(used)):
            a, b = used[i - 1], used[i]
            val = round(random.uniform(0.5, 5.0), 2)
            equations.append([a, b])
            values.append(val)

        for _ in range(max(0, num_equations - len(equations))):
            if len(used) < 2:
                break
            a, b = random.sample(used, 2)
            implied_graph = {}
            for (x, y), v in zip(equations, values):
                implied_graph.setdefault(x, {})[y] = v
                implied_graph.setdefault(y, {})[x] = 1.0 / v

            def implied_ratio(src, dst, visited):
                visited.add(src)
                for nxt, w in implied_graph.get(src, {}).items():
                    if nxt in visited:
                        continue
                    if nxt == dst:
                        return w
                    sub = implied_ratio(nxt, dst, visited)
                    if sub is not None:
                        return w * sub
                return None

            val = implied_ratio(a, b, set())
            equations.append([a, b])
            values.append(val)

        queries = []
        for _ in range(num_queries):
            c = random.choice(variables)
            d = random.choice(variables)
            queries.append([c, d])

        return equations, values, queries

    random.seed(42)
    trials = 300
    for t in range(trials):
        num_vars = random.randint(2, 10)
        equations, values, queries = random_equations_and_queries(
            num_vars, random.randint(1, 8), random.randint(1, 10)
        )

        expected = brute_force(equations, values, queries)
        actual = solve(equations, values, queries)

        for e, a in zip(expected, actual):
            ok = (e == -1.0 and a == -1.0) or abs(e - a) < 1e-6
            assert ok, (
                f"mismatch on trial {t}: equations={equations}, values={values}, "
                f"queries={queries}\nexpected={expected}\nactual={actual}"
            )

    print(f"Stress test passed: {trials} trials.")
