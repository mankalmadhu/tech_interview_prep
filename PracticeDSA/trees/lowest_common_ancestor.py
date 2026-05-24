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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

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
    
    # Test 1: p=5, q=1 -> LCA=3
    print("Test 1:", sol.lowestCommonAncestor(root, root.left, root.right).val == 3)
    
    # Test 2: p=5, q=2 -> LCA=5
    print("Test 2:", sol.lowestCommonAncestor(root, root.left, root.left.right).val == 5)
