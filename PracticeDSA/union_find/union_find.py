"""
Union-Find (Disjoint Set Union)

Supports, over a fixed set of elements (arbitrary hashable values,
not necessarily 0..n-1):
  - find(x): return the representative/root of x's set
  - union(x, y): merge the sets containing x and y
  - connected(x, y): are x and y in the same set?

Backed by a single dict `parent_lookup[x] = (parent, size)`. An
element whose own value equals its stored parent is a root; `size`
is only meaningful (and kept up to date) on root entries.

Two optimizations are combined:

1. Path compression (in `find`): after locating the root, every node
   visited along the climb has its parent pointer rewritten directly
   to the root, so future `find` calls on those same nodes are O(1).

2. Union by size (in `union`): the root of the smaller tree is
   always attached under the root of the larger tree, and the
   surviving root's size is updated to the combined total. This
   bounds tree height to O(log n) even before any path compression
   has had a chance to flatten things.

Combined, these two optimizations give amortized O(a(n)) per
operation, where a is the inverse Ackermann function - for any
practical n this is effectively a small constant (<= 4-5), so "near
O(1)" is a fair practical shorthand. Without either optimization, a
long chain of unions can degrade `find` to O(n) per call (e.g.
union(1,2), union(2,3), union(3,4), ... forms a straight-line chain).

Complexity Analysis:
--------------------
Time:  O(a(n)) amortized per find/union/connected call (near O(1)
       in practice), thanks to path compression + union by size
       together.
Space: O(n) for the parent_lookup dict (one entry per element).
"""


class UnionFind:
    def __init__(self, elements):
        self.parent_lookup = {el: (el, 0,1) for el in elements}

    def _find_with_weight(self, x):

        cur = x
        path_to_root = []
        while self.parent_lookup[cur][0] != cur:
            path_to_root.append(cur)
            cur = self.parent_lookup[cur][0]
        root = cur

        # path compression: point every visited node directly at root
        for cur in reversed(path_to_root):
            next_cur = self.parent_lookup[cur][0]
            new_weight = self.parent_lookup[cur][2] * self.parent_lookup[next_cur][2]
            self.parent_lookup[cur] = (root, self.parent_lookup[cur][1],new_weight)

        return root, self.parent_lookup[x][2]


    def find(self, x):
        if x not in self.parent_lookup:
            return None
        root, _ = self._find_with_weight(x)
        return root

    def get_node_weight(self, x):
        _, weight = self._find_with_weight(x)
        return weight


    def union(self, x, y, weight=1.0):
        if x not in self.parent_lookup or y not in self.parent_lookup:
            return

        root_x, weight_x= self._find_with_weight(x)
        root_y ,weight_y= self._find_with_weight(y)
        if root_x == root_y:
            return

        _, size_x,_ = self.parent_lookup[root_x]
        _, size_y,_ = self.parent_lookup[root_y]
        new_weight = weight_x / (weight * weight_y)

        # union by size: attach smaller tree under larger tree's root
        if size_x >= size_y:
            self.parent_lookup[root_y] = (root_x, size_x + size_y, new_weight)
        else:
            self.parent_lookup[root_x] = (root_y, size_x + size_y,1/new_weight)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind([17, 42, 3, 99, 256])
    uf.union(17, 42)
    uf.union(3, 99)
    uf.union(42, 3)

    assert uf.connected(17, 99) is True
    assert uf.connected(17, 256) is False

    # element 0 edge case (falsy value, must not be mistaken for None)
    uf0 = UnionFind([0, 1, 2])
    uf0.union(0, 1)
    assert uf0.connected(0, 1) is True
    assert uf0.connected(0, 2) is False

    print("Example tests passed!")

    # ---- direct weight-chain test (bypasses union, checks compression) ----
    uf_w = UnionFind(["a", "b", "c", "root"])
    uf_w.parent_lookup["a"] = ("b", 0, 2)
    uf_w.parent_lookup["b"] = ("c", 0, 3)
    uf_w.parent_lookup["c"] = ("root", 0, 5)
    uf_w.parent_lookup["root"] = ("root", 0, 1)

    root, weight = uf_w._find_with_weight("a")
    assert root == "root", f"expected root='root', got {root}"
    assert abs(weight - 30) < 1e-9, f"expected weight=30, got {weight}"
    # confirm path compression actually flattened a and b to point at root
    assert uf_w.parent_lookup["a"][0] == "root"
    assert uf_w.parent_lookup["b"][0] == "root"
    assert abs(uf_w.parent_lookup["b"][2] - 15) < 1e-9

    print("Weight-chain test passed!")

    # ---- stress test vs independent brute-force groups ----
    import random

    class BruteForceGroups:
        """Independent reference: tracks groups as plain Python sets.
        union merges the two groups containing x and y; connected
        just checks whether x and y land in the same group set.
        Doesn't reuse any parent-pointer/find logic at all."""

        def __init__(self, elements):
            self.groups = [{el} for el in elements]

        def _group_index(self, x):
            for i, g in enumerate(self.groups):
                if x in g:
                    return i
            return None

        def union(self, x, y):
            i, j = self._group_index(x), self._group_index(y)
            if i is None or j is None or i == j:
                return
            self.groups[i] |= self.groups[j]
            del self.groups[j]

        def connected(self, x, y):
            i, j = self._group_index(x), self._group_index(y)
            return i is not None and i == j

    random.seed(42)
    trials = 300
    for t in range(trials):
        n = random.randint(1, 12)
        elements = list(range(n))
        random.shuffle(elements)

        uf = UnionFind(elements)
        bf = BruteForceGroups(elements)

        num_ops = random.randint(0, 20)
        for _ in range(num_ops):
            x, y = random.choice(elements), random.choice(elements)
            uf.union(x, y)
            bf.union(x, y)

        for _ in range(20):
            x, y = random.choice(elements), random.choice(elements)
            expected = bf.connected(x, y)
            actual = uf.connected(x, y)
            assert expected == actual, (
                f"mismatch on trial {t}: connected({x},{y}) "
                f"expected={expected} actual={actual}, elements={elements}"
            )

    print(f"Stress test passed: {trials} trials.")

    # ---- weighted stress test vs independent brute-force graph ----
    class BruteForceWeightedGraph:
        """Independent reference: builds its own weighted adjacency
        graph (two directed edges per union: x->y with value, y->x
        with 1/value), then DFS's between two nodes multiplying edge
        weights along the path. Doesn't reuse any parent-pointer/
        weight-compression logic at all."""

        def __init__(self, elements):
            self.graph = {el: {} for el in elements}

        def ratio(self, x, y):
            if x == y:
                return 1.0

            def dfs(src, dst, visited):
                visited.add(src)
                for nxt, w in self.graph[src].items():
                    if nxt in visited:
                        continue
                    if nxt == dst:
                        return w
                    sub = dfs(nxt, dst, visited)
                    if sub is not None:
                        return w * sub
                return None

            return dfs(x, y, set())

        def union(self, x, y, value):
            # mirror real union-find semantics: a redundant union on
            # an already-connected pair is a no-op (first-established
            # ratio wins), otherwise the test's own random values could
            # create an inconsistent graph with conflicting paths.
            if self.ratio(x, y) is not None:
                return
            self.graph[x][y] = value
            self.graph[y][x] = 1.0 / value

    random.seed(7)
    trials = 300
    for t in range(trials):
        n = random.randint(2, 10)
        elements = [f"n{i}" for i in range(n)]

        uf = UnionFind(elements)
        bf = BruteForceWeightedGraph(elements)

        num_ops = random.randint(0, 15)
        for _ in range(num_ops):
            x, y = random.sample(elements, 2)
            value = round(random.uniform(0.1, 10.0), 3)
            uf.union(x, y, value)
            bf.union(x, y, value)

        for _ in range(20):
            x, y = random.sample(elements, 2)
            expected_ratio = bf.ratio(x, y)
            connected = uf.connected(x, y)

            if expected_ratio is None:
                assert not connected, (
                    f"mismatch on trial {t}: {x}/{y} expected disconnected, "
                    f"but uf says connected, elements={elements}"
                )
            else:
                assert connected, (
                    f"mismatch on trial {t}: {x}/{y} expected connected "
                    f"(ratio={expected_ratio}), but uf says disconnected"
                )
                actual_ratio = uf.get_node_weight(x) / uf.get_node_weight(y)
                assert abs(actual_ratio - expected_ratio) < 1e-6, (
                    f"mismatch on trial {t}: {x}/{y} expected={expected_ratio} "
                    f"actual={actual_ratio}, elements={elements}"
                )

    print(f"Weighted stress test passed: {trials} trials.")
