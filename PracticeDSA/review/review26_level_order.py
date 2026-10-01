"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/trees/level_order_traversal.py until you're done.

Problem (Binary Tree Level Order Traversal, LeetCode 102):

Given the root of a binary tree, return the level order traversal
of its nodes' values (i.e., from left to right, level by level).

Example:
       3
     /   \
    9     20
         /  \
        15   7

  -> [[3], [9, 20], [15, 7]]

Write your solution below (BFS using a queue).
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        q = deque([root])

        cur_node = None
        result=[]

        if not root:
            return result

        while q:
            l = len(q)
            level = []
            for i in range(l):
                cur_node = q.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            result.append(level)

        return result

    def levelOrderList(self, root):
        stack = [root]

        result=[]

        if not root:
            return result

        while stack:
            level = []
            cur_node = None

            for i in range(len(stack)):
                cur_node = stack.pop(0)
                level.append(cur_node.val)
                if cur_node.left:
                    stack.append(cur_node.left)
                if cur_node.right:
                    stack.append(cur_node.right)
            result.append(level)

        return result



if __name__ == "__main__":
    sol = Solution()

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    print("Test 1:", sol.levelOrderList(root1), "Expected: [[3], [9, 20], [15, 7]]")
    print("Test 2:", sol.levelOrder(TreeNode(1)), "Expected: [[1]]")
    print("Test 3:", sol.levelOrder(None), "Expected: []")

    assert sol.levelOrder(root1) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrder(TreeNode(1)) == [[1]]
    assert sol.levelOrder(None) == []

    def dfs_level_order(root):
        """Ground truth via recursive DFS, tracking depth."""
        levels = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(levels):
                levels.append([])
            levels[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return levels

    import random

    def build_random_tree(nodes_left, next_val):
        if nodes_left == 0:
            return None
        r = TreeNode(next_val[0])
        next_val[0] += 1
        nodes_left -= 1
        left_count = random.randint(0, nodes_left)
        right_count = nodes_left - left_count
        r.left = build_random_tree(left_count, next_val)
        r.right = build_random_tree(right_count, next_val)
        return r

    for _ in range(500):
        n = random.randint(0, 30)
        root = build_random_tree(n, [0])
        got = sol.levelOrder(root)
        want = dfs_level_order(root)
        assert got == want, f"mismatch: got {got}, want {want}"
    print("500 randomized trials passed (deque version)")

    for _ in range(500):
        n = random.randint(0, 30)
        root = build_random_tree(n, [0])
        got = sol.levelOrderList(root)
        want = dfs_level_order(root)
        assert got == want, f"mismatch: got {got}, want {want}"
    print("500 randomized trials passed (plain-list version)")
