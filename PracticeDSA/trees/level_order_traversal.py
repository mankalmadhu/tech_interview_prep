# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        """
        Returns the level order traversal of a binary tree's nodes' values.

        Algorithm: Breadth-First Search (BFS) using a Queue
        - Time Complexity: O(N) where N is the number of nodes. We visit every node exactly once.
        - Space Complexity: O(N). In the worst case (a perfectly balanced tree), the leaf level
          holds up to N/2 nodes in the queue simultaneously.

        Implementation Note:
        - We use collections.deque for O(1) pops from the left.
        - Taking `l = len(q)` strictly at the start of the while loop guarantees we only process
          nodes from the current level before moving on to the children.
        """
        res = []
        if not root:
            return res

        q = deque([root])
        while q:
            l = len(q)
            level = []
            for i in range(l):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
        return res

    def levelOrderList(self, root) -> list[list[int]]:
        """
        Same BFS logic, but using a plain Python list as the queue instead
        of collections.deque, popping from the front with pop(0).

        Correctness nuance: use pop(0) (always front), NOT pop(i) with an
        incrementing index. Each pop(0) shifts the remaining list left, so
        tracking position by a separate counter index gets out of sync and
        silently skips/misorders elements.

        Time Complexity: O(N^2) worst case -- list.pop(0) is O(k) per call
        (it must shift all remaining elements), unlike deque.popleft()'s
        O(1). Space Complexity: O(N), same as the deque version.
        """
        res = []
        if not root:
            return res

        q = [root]
        while q:
            l = len(q)
            level = []
            for i in range(l):
                node = q.pop(0)
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)
        return res


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    sol = Solution()

    # Test 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("Test 1:", sol.levelOrder(root1))

    # Test 2: [1]
    print("Test 2:", sol.levelOrder(TreeNode(1)))

    # Test 3: []
    print("Test 3:", sol.levelOrder(None))

    assert sol.levelOrder(root1) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrder(TreeNode(1)) == [[1]]
    assert sol.levelOrder(None) == []
    assert sol.levelOrderList(root1) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrderList(TreeNode(1)) == [[1]]
    assert sol.levelOrderList(None) == []
    print("fixed cases passed")

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
        rand_root = build_random_tree(n, [0])
        want = dfs_level_order(rand_root)
        assert sol.levelOrder(rand_root) == want
        assert sol.levelOrderList(rand_root) == want
    print("500 randomized trials passed (deque + plain-list versions)")
