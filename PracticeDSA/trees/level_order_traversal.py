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
        if not root: return res

        q = deque([root])
        while q:
            l = len(q)
            level = []
            for i in range(l):
                node = q.popleft()
                level.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            res.append(level)
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == '__main__':
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