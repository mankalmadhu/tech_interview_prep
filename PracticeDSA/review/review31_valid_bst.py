"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/trees/valid_bst.py until you're done.

Problem (Validate Binary Search Tree, LeetCode 98):

Given the root of a binary tree, determine if it is a valid binary
search tree (BST). A valid BST means: for every node, ALL values in
its left subtree are strictly less than the node's value, and ALL
values in its right subtree are strictly greater -- not just the
node's immediate children.

Example (INVALID, despite each node's immediate children looking ok):
      5
    /   \
   1     4
       /   \
      3     6
  -> False (4 and 3 are both < 5, but sit in 5's right subtree)

Example (valid):
      5
    /   \
   3     8
       /   \
      6     9
  -> True

Write your solution below (DFS passing down a (min, max) valid range).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        return self.dfs(root, float('-inf'),float('inf'))

    def dfs(self, node, l_val, r_val):

        if not node:
            return True

        if node.val <= l_val or node.val >=r_val:
            return False

        return self.dfs(node.left,l_val, node.val) and self.dfs(node.right,node.val,r_val)

    def isValidBSTIt(self, root):
        stack = []
        cur_node = root
        prev_val = float('-inf')

        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            cur_node = stack.pop()
            if cur_node.val <= prev_val:
                return False
            prev_val = cur_node.val
            cur_node = cur_node.right

        return True


if __name__ == "__main__":
    sol = Solution()

    # valid: 5 -> (3, 8 -> (6, 9))
    valid_root = TreeNode(5)
    valid_root.left = TreeNode(3)
    valid_root.right = TreeNode(8)
    valid_root.right.left = TreeNode(6)
    valid_root.right.right = TreeNode(9)
    assert sol.isValidBST(valid_root) is True

    print(sol.isValidBSTIt(valid_root))

    # invalid: 5 -> (1, 4 -> (3, 6))
    invalid_root = TreeNode(5)
    invalid_root.left = TreeNode(1)
    invalid_root.right = TreeNode(4)
    invalid_root.right.left = TreeNode(3)
    invalid_root.right.right = TreeNode(6)
    assert sol.isValidBST(invalid_root) is False

    # single node
    assert sol.isValidBST(TreeNode(1)) is True

    # equal values (not strictly less/greater -> invalid)
    eq_root = TreeNode(2)
    eq_root.left = TreeNode(2)
    assert sol.isValidBST(eq_root) is False

    # empty tree
    assert sol.isValidBST(None) is True

    print("fixed cases passed")

    import random

    def brute_force(root):
        """Ground truth: collect in-order values, check strictly increasing."""
        vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)
        return all(vals[i] < vals[i + 1] for i in range(len(vals) - 1))

    def build_random_tree(nodes_left, next_val):
        if nodes_left == 0:
            return None
        r = TreeNode(next_val())
        nodes_left -= 1
        left_count = random.randint(0, nodes_left)
        right_count = nodes_left - left_count
        r.left = build_random_tree(left_count, next_val)
        r.right = build_random_tree(right_count, next_val)
        return r

    for _ in range(500):
        n = random.randint(0, 20)
        root = build_random_tree(n, lambda: random.randint(0, 10))
        got = sol.isValidBST(root)
        want = brute_force(root)
        assert got == want, f"mismatch for tree with n={n}: got {got}, want {want}"
    print("500 randomized trials passed (recursive)")

    for _ in range(500):
        n = random.randint(0, 20)
        root = build_random_tree(n, lambda: random.randint(0, 10))
        got_it = sol.isValidBSTIt(root)
        want = brute_force(root)
        assert got_it == want, f"mismatch for tree with n={n}: got {got_it}, want {want}"
    print("500 randomized trials passed (iterative)")
