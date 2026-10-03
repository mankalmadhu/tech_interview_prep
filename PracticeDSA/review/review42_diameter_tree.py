"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/trees/diameter_tree.py until you're done.

Problem (Diameter of Binary Tree, LeetCode 543):

Given the root of a binary tree, return the length of the diameter
of the tree.

The diameter of a binary tree is the length of the longest path
between any two nodes in the tree. This path may or may not pass
through the root. The length of a path between two nodes is
represented by the number of edges between them.

Example:
      1
     / \\
    2   3
   / \\
  4   5

  diameter = 3 (path: 4 -> 2 -> 1 -> 3, or 4 -> 2 -> 5, both have 3 edges)

Write your solution below.
"""


def diameter_of_binary_tree(root):
    max_dia = 0

    def __dfs(node):
        nonlocal max_dia
        if not node:
            return 0

        l_depth = __dfs(node.left)
        r_depth = __dfs(node.right)
        max_dia = max(max_dia, l_depth+r_depth)

        return 1 + max(l_depth, r_depth)

    __dfs(root)
    return max_dia

def bst_dia_it(root):

    if not root:
        return 0

    stack1 = [root]
    stack2 = []

    while stack1:
        elem = stack1.pop()
        stack2.append(elem)
        if elem.left:
            stack1.append(elem.left)
        if elem.right:
            stack1.append(elem.right)

    heights = {}
    max_dia = 0

    for node in reversed(stack2):
        l_depth = heights.get(node.left,0)
        r_depth = heights.get(node.right,0)
        heights[node] = 1 + max(l_depth, r_depth)
        max_dia = max(max_dia, l_depth + r_depth)

    return max_dia





if __name__ == "__main__":
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = Node(1, Node(2, Node(4), Node(5)), Node(3))
    fixed_cases = [
        (root, 3),
        (Node(1), 0),
        (None, 0),
        (Node(1, Node(2, Node(3, Node(4)))), 3),  # skewed left, diameter = full chain
    ]
    for tree, expected in fixed_cases:
        got = diameter_of_binary_tree(tree)
        assert got == expected, f"expected {expected}, got {got}"
    print("fixed cases passed")

    print(bst_dia_it(fixed_cases[0][0]))

    import random

    def brute_force(node):
        # independent O(N^2)-ish re-derivation: height() + separate max-over-nodes scan
        def height(n):
            if not n:
                return 0
            return 1 + max(height(n.left), height(n.right))

        def collect_nodes(n, acc):
            if not n:
                return
            acc.append(n)
            collect_nodes(n.left, acc)
            collect_nodes(n.right, acc)

        nodes = []
        collect_nodes(node, nodes)
        best = 0
        for n in nodes:
            best = max(best, height(n.left) + height(n.right))
        return best

    def build_random_tree(n):
        if n == 0:
            return None
        nodes = [Node(i) for i in range(n)]
        for i in range(1, n):
            parent = nodes[random.randint(0, i - 1)]
            if parent.left is None and random.random() < 0.5:
                parent.left = nodes[i]
            elif parent.right is None:
                parent.right = nodes[i]
            else:
                parent.left = nodes[i]
        return nodes[0]

    for _ in range(300):
        n = random.randint(0, 12)
        tree = build_random_tree(n)
        got = diameter_of_binary_tree(tree)
        want = brute_force(tree)
        assert got == want, f"n={n}: expected {want}, got {got}"
    print("300 randomized trials passed")

    for tree, expected in fixed_cases:
        got = bst_dia_it(tree)
        assert got == expected, f"bst_dia_it: expected {expected}, got {got}"
    print("bst_dia_it fixed cases passed")

    for _ in range(300):
        n = random.randint(0, 12)
        tree = build_random_tree(n)
        got = bst_dia_it(tree)
        want = brute_force(tree)
        assert got == want, f"n={n}: expected {want}, got {got}"
    print("bst_dia_it 300 randomized trials passed")
