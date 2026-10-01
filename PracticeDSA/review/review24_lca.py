"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/trees/lowest_common_ancestor.py until you're done.

Problem (Lowest Common Ancestor of a Binary Tree, LeetCode 236):

Given a binary tree and two nodes p and q (both guaranteed to exist
in the tree), find their lowest common ancestor (LCA) — the deepest
node that has both p and q as descendants (a node is allowed to be
its own descendant).

Example tree:
       3
     /   \
    5     1
   / \   / \
  6   2 0   8

  LCA(5, 1) -> 3
  LCA(5, 2) -> 5

Write your solution below (DFS, post-order).
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if not root:
            return

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root

        return left if left else right

    def lowetCommonAncestorIterative(self, root, p ,q):

        desc_parent_lookup = {}

        stack =[root]
        cur = None

        while stack:
            cur = stack.pop()
            if cur.left:
                desc_parent_lookup[cur.left] = cur
                stack.append(cur.left)

            if cur.right:
                desc_parent_lookup[cur.right] = cur
                stack.append(cur.right)

        cur_child = p
        p_parent_lookup = {p}
        while (cur_child in desc_parent_lookup):
            desc = desc_parent_lookup[cur_child]
            p_parent_lookup.add(desc)
            cur_child = desc

        cur_child = q

        if p_parent_lookup:
            if cur_child in p_parent_lookup:
                return cur_child
            while (cur_child in desc_parent_lookup):
                desc = desc_parent_lookup[cur_child]
                if desc in p_parent_lookup:
                    return desc
                cur_child = desc






if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    assert sol.lowestCommonAncestor(root, root.left, root.right).val == 3
    assert sol.lowestCommonAncestor(root, root.left, root.left.right).val == 5
    assert sol.lowestCommonAncestor(root, root.left.left, root.left.right.right).val == 5
    assert sol.lowestCommonAncestor(root, root.left.right.left, root.left.right.right).val == 2
    assert sol.lowestCommonAncestor(root, root, root.right.right).val == 3
    print("fixed cases passed")

    assert sol.lowetCommonAncestorIterative(root, root.left, root.right).val == 3
    assert sol.lowetCommonAncestorIterative(root, root.left, root.left.right).val == 5
    assert sol.lowetCommonAncestorIterative(root, root.left.left, root.left.right.right).val == 5
    assert sol.lowetCommonAncestorIterative(root, root.left.right.left, root.left.right.right).val == 2
    assert sol.lowetCommonAncestorIterative(root, root, root.right.right).val == 3
    print("iterative fixed cases passed")

    import random

    def build_random_tree(nodes_left, next_val):
        """Builds a random tree, returns (root, list_of_all_nodes)."""
        if nodes_left == 0:
            return None, []
        root = TreeNode(next_val[0])
        next_val[0] += 1
        nodes_left -= 1
        left_count = random.randint(0, nodes_left)
        right_count = nodes_left - left_count
        root.left, left_nodes = build_random_tree(left_count, next_val)
        root.right, right_nodes = build_random_tree(right_count, next_val)
        return root, [root] + left_nodes + right_nodes

    for _ in range(500):
        n = random.randint(2, 30)
        root, all_nodes = build_random_tree(n, [0])
        p, q = random.sample(all_nodes, 2)
        rec = sol.lowestCommonAncestor(root, p, q)
        it = sol.lowetCommonAncestorIterative(root, p, q)
        assert rec is it, f"mismatch for p={p.val}, q={q.val}: rec={rec.val}, it={it.val}"
    print("500 randomized trials passed (recursive vs iterative agree)")
