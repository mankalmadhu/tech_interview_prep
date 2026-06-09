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
        return self.dfs_rec(root, float('-inf'), float('inf'))
        # TODO: Implement In-Order Traversal approach next review

    def dfs_rec(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return self.dfs_rec(node.left, min_val, node.val) and self.dfs_rec(node.right, node.val, max_val)
