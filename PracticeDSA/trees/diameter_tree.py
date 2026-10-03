from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_dia = float("-inf")

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Finds the length of the diameter of the tree.
        The diameter is the length of the longest path between any two nodes.

        Discussion Summary:
        - The longest path in a tree does not necessarily pass through the root.
        - However, every path "arches" over some specific node acting as its local peak.
        - The length of the longest path arching over any given node is simply:
          (max depth of its left subtree) + (max depth of its right subtree)
        - We use a recursive DFS that calculates the depth of each node from the bottom up.
        - As the DFS bubbles up the depths to the parent, we simultaneously update a
          global `self.max_dia` tracker if the current node's local diameter is larger.

        Time Complexity: O(N)
        - We visit every single node in the tree exactly once.

        Space Complexity: O(N) worst-case
        - The recursive call stack can reach O(N) in a completely skewed, unbalanced tree.
          For a perfectly balanced tree, it would be O(log N).

        Key Insight:
        ----------------
        At every node, we calculate two things:

        1. The diameter passing through the current node =
           left_height + right_height  (edges)

        2. The height of the current subtree (needed by parent nodes) =
           1 + max(left_height, right_height)

        Why `return 1 + max(left, right)`?
        -----------------------------------
        This function returns the **height** of the subtree rooted at current node.
        Height is measured as number of nodes along the longest path from
        this node down to a leaf. Hence we add 1 for the current node itself.

        This returned height is used by the parent node to compute its own
        diameter and height.
        """
        self.max_dia = 0
        self.dfs_rec(root)
        return self.max_dia

    def dfs_rec(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth = self.dfs_rec(node.left)
        right_depth = self.dfs_rec(node.right)

        # The local diameter peaking at this node
        self.max_dia = max(self.max_dia, left_depth + right_depth)

        # Return the actual depth to the parent
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTreeIterative(self, root: Optional[TreeNode]) -> int:
        """
        Iterative version using an explicit two-stack post-order traversal.

        Height must be computed bottom-up (children before parent), which is
        exactly post-order's "left, right, node" ordering. To get a
        parent-after-children visit order without recursion, we use the
        classic two-stack trick:
          - Pop from stack1, push onto stack2, then push left then right
            onto stack1 (so right is popped before left).
          - stack2 ends up in a "parent, then descendants" order; iterating
            it in reverse guarantees every node's children are processed
            before the node itself.

        At each node (processed in that reversed order) we look up its
        children's already-computed heights, update the global diameter
        using left_height + right_height (a sum, NOT the node's own height),
        and store this node's own height (1 + max(left, right)) for its
        ancestors to use later.

        Time Complexity: O(N) - each node is pushed/popped/visited a
        constant number of times across both stacks.

        Space Complexity: O(N) always - stack1, stack2, and the heights
        dict each hold up to N entries, regardless of tree shape. This is
        strictly worse-or-equal to the recursive version's O(H) call stack,
        which can be as low as O(log N) for a balanced tree.
        """
        if not root:
            return 0

        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        heights = {}
        max_dia = 0

        for node in reversed(stack2):
            left_height = heights.get(node.left, 0)
            right_height = heights.get(node.right, 0)
            heights[node] = 1 + max(left_height, right_height)
            max_dia = max(max_dia, left_height + right_height)

        return max_dia


if __name__ == "__main__":
    import random

    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    fixed_cases = [
        (root, 3),
        (TreeNode(1), 0),
        (None, 0),
        (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)))), 3),  # left-skewed chain
    ]

    for tree, expected in fixed_cases:
        got_rec = Solution().diameterOfBinaryTree(tree)
        got_it = Solution().diameterOfBinaryTreeIterative(tree)
        assert got_rec == expected, f"recursive: expected {expected}, got {got_rec}"
        assert got_it == expected, f"iterative: expected {expected}, got {got_it}"
    print("fixed cases passed (recursive + iterative)")

    def brute_force(node):
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
        nodes = [TreeNode(i) for i in range(n)]
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
        want = brute_force(tree)
        got_rec = Solution().diameterOfBinaryTree(tree)
        got_it = Solution().diameterOfBinaryTreeIterative(tree)
        assert got_rec == want, f"recursive n={n}: expected {want}, got {got_rec}"
        assert got_it == want, f"iterative n={n}: expected {want}, got {got_it}"
    print("300 randomized trials passed (recursive + iterative)")
