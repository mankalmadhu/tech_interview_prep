from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_dia = float('-inf')
    
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
