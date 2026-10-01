class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Discussion & Logic:
- We use Depth First Search (DFS) post-order traversal to propagate information up the tree.
- If we hit a null node, we return None.
- If the current node matches either `p` or `q`, we return the current node immediately to its parent.
- We recursively search the left and right subtrees.
- If BOTH left and right recursive calls return a non-null node, it means `p` is in one subtree and `q` is in the other. This makes the current node the Lowest Common Ancestor!
- If only ONE of the recursive calls returns a node, we pass that node further up the chain.
- Edge Case Warning: This logic strictly assumes both `p` and `q` exist in the tree. If only `p` exists, the algorithm returns `p` incorrectly as the LCA because it stops searching the subtree once it finds `p`.
  *Fix for un-guaranteed nodes (LCA II)*: To handle nodes that might not exist, you must stop short-circuiting. You can either (1) traverse the entire tree without returning early to track `p_found` and `q_found` booleans, or (2) run a separate O(N) `exists(root, node)` helper function first to verify both nodes are in the tree.

Complexity Analysis:
- Time Complexity: O(N) where N is the number of nodes. In the worst case, we must visit every node to find `p` and `q`.
- Space Complexity: O(H) where H is the height of the tree. This is the auxiliary space used by the recursion call stack. In the worst case (a completely unbalanced, linked-list-like tree), this degrades to O(N).
"""


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if not root:
            return

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right

    def lowestCommonAncestorIterative(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Iterative alternative: build a child->parent map via iterative DFS,
        walk up from p collecting all its ancestors (including itself),
        then walk up from q until hitting the first node already in that
        ancestor set. Trades O(H) recursion-stack space for guaranteed
        O(N) heap space, avoiding stack-overflow risk on deep/skewed trees.
        Time: O(N) | Space: O(N)
        """
        child_to_parent = {}
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.left:
                child_to_parent[cur.left] = cur
                stack.append(cur.left)
            if cur.right:
                child_to_parent[cur.right] = cur
                stack.append(cur.right)

        p_ancestors = {p}
        cur_child = p
        while cur_child in child_to_parent:
            cur_child = child_to_parent[cur_child]
            p_ancestors.add(cur_child)

        cur_child = q
        while True:
            if cur_child in p_ancestors:
                return cur_child
            if cur_child not in child_to_parent:
                return None
            cur_child = child_to_parent[cur_child]


if __name__ == "__main__":
    sol = Solution()
    # Create tree:
    #      3
    #    /   \
    #   5     1
    #  / \   / \
    # 6   2 0   8
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Test 1: p=5, q=1 -> LCA=3
    print("Test 1:", sol.lowestCommonAncestor(root, root.left, root.right).val == 3)

    # Test 2: p=5, q=2 -> LCA=5
    print(
        "Test 2:", sol.lowestCommonAncestor(root, root.left, root.left.right).val == 5
    )

    assert sol.lowestCommonAncestor(root, root.left, root.right).val == 3
    assert sol.lowestCommonAncestor(root, root.left, root.left.right).val == 5
    assert sol.lowestCommonAncestor(root, root.left.left, root.left.right.right).val == 5
    assert sol.lowestCommonAncestor(root, root.left.right.left, root.left.right.right).val == 2
    assert sol.lowestCommonAncestor(root, root, root.right.right).val == 3

    assert sol.lowestCommonAncestorIterative(root, root.left, root.right).val == 3
    assert sol.lowestCommonAncestorIterative(root, root.left, root.left.right).val == 5
    assert sol.lowestCommonAncestorIterative(root, root.left.left, root.left.right.right).val == 5
    assert sol.lowestCommonAncestorIterative(root, root.left.right.left, root.left.right.right).val == 2
    assert sol.lowestCommonAncestorIterative(root, root, root.right.right).val == 3
    print("fixed cases passed (recursive + iterative)")

    import random

    def build_random_tree(nodes_left, next_val):
        if nodes_left == 0:
            return None, []
        r = TreeNode(next_val[0])
        next_val[0] += 1
        nodes_left -= 1
        left_count = random.randint(0, nodes_left)
        right_count = nodes_left - left_count
        r.left, left_nodes = build_random_tree(left_count, next_val)
        r.right, right_nodes = build_random_tree(right_count, next_val)
        return r, [r] + left_nodes + right_nodes

    for _ in range(500):
        n = random.randint(2, 30)
        rand_root, all_nodes = build_random_tree(n, [0])
        rp, rq = random.sample(all_nodes, 2)
        rec = sol.lowestCommonAncestor(rand_root, rp, rq)
        it = sol.lowestCommonAncestorIterative(rand_root, rp, rq)
        assert rec is it, f"mismatch for p={rp.val}, q={rq.val}: rec={rec.val}, it={it.val}"
    print("500 randomized trials passed (recursive vs iterative agree)")
