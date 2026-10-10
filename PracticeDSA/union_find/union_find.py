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
        self.parent_lookup = {el: (el, 0) for el in elements}

    def find(self, x):
        if x not in self.parent_lookup:
            return None

        cur = x
        while self.parent_lookup[cur][0] != cur:
            cur = self.parent_lookup[cur][0]
        root = cur

        # path compression: point every visited node directly at root
        cur = x
        while self.parent_lookup[cur][0] != cur:
            next_cur = self.parent_lookup[cur][0]
            self.parent_lookup[cur] = (root, self.parent_lookup[cur][1])
            cur = next_cur

        return root

    def union(self, x, y):
        if x not in self.parent_lookup or y not in self.parent_lookup:
            return

        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        _, size_x = self.parent_lookup[root_x]
        _, size_y = self.parent_lookup[root_y]

        # union by size: attach smaller tree under larger tree's root
        if size_x >= size_y:
            self.parent_lookup[root_y] = (root_x, size_x + size_y)
        else:
            self.parent_lookup[root_x] = (root_y, size_x + size_y)

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
