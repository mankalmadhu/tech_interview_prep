from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).

        Discussion Summary:
        - A common mistake is only checking if a node's immediate children are valid
          (node.left.val < node.val < node.right.val).
        - This fails because a node must be valid against the constraints of ALL its ancestors
          (e.g., a node deep in the right subtree of the root must still be > root.val).
        - To solve this, we use a recursive DFS approach that passes down 'min_val' and 'max_val'
          bounds.
        - When branching left, the current node's value becomes the new 'max_val'.
        - When branching right, the current node's value becomes the new 'min_val'.

        Time Complexity: O(N)
        - We visit each node in the tree exactly once.

        Space Complexity: O(N) worst-case
        - In the worst case (a completely unbalanced, skewed tree), the recursion stack
          will grow to O(N). In the best case (a perfectly balanced tree), it is O(log N).
        """
        return self.dfs_rec(root, float("-inf"), float("inf"))

    def dfs_rec(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return self.dfs_rec(node.left, min_val, node.val) and self.dfs_rec(
            node.right, node.val, max_val
        )

    def isValidBSTIterative(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative alternative: in-order traversal using an explicit stack.
        A tree is a valid BST if and only if its in-order traversal visits
        values in strictly increasing order. We only need to track the
        previously-visited value (prev_val), not the full list -- each new
        value just needs to be strictly greater than the last one seen.

        Time Complexity: O(N) | Space Complexity: O(H) for the stack
        (H = tree height; worst case O(N) for a skewed tree).
        """
        stack = []
        cur_node = root
        prev_val = float("-inf")

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

    valid_root = TreeNode(5)
    valid_root.left = TreeNode(3)
    valid_root.right = TreeNode(8)
    valid_root.right.left = TreeNode(6)
    valid_root.right.right = TreeNode(9)
    assert sol.isValidBST(valid_root) is True
    assert sol.isValidBSTIterative(valid_root) is True

    invalid_root = TreeNode(5)
    invalid_root.left = TreeNode(1)
    invalid_root.right = TreeNode(4)
    invalid_root.right.left = TreeNode(3)
    invalid_root.right.right = TreeNode(6)
    assert sol.isValidBST(invalid_root) is False
    assert sol.isValidBSTIterative(invalid_root) is False

    assert sol.isValidBST(TreeNode(1)) is True
    assert sol.isValidBSTIterative(TreeNode(1)) is True

    eq_root = TreeNode(2)
    eq_root.left = TreeNode(2)
    assert sol.isValidBST(eq_root) is False
    assert sol.isValidBSTIterative(eq_root) is False

    assert sol.isValidBST(None) is True
    assert sol.isValidBSTIterative(None) is True

    print("fixed cases passed")

    import random

    def brute_force(root):
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
        rand_root = build_random_tree(n, lambda: random.randint(0, 10))
        want = brute_force(rand_root)
        assert sol.isValidBST(rand_root) == want
        assert sol.isValidBSTIterative(rand_root) == want
    print("500 randomized trials passed (recursive + iterative)")
