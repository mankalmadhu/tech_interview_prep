class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Inverts a binary tree by swapping the left and right children of every node.
    
    Time Complexity: O(N)
    - We must visit every single node in the tree exactly once to invert its children.
    
    Space Complexity: O(H) where H is the height of the tree.
    - This is the maximum depth of the recursive call stack. In the worst-case 
      (a completely unbalanced tree), H could be N, leading to an O(N) space 
      complexity and a potential RecursionError (Stack Overflow).
      
    Logic & Trade-offs:
    - We use a recursive DFS approach.
    - Base case: If the root is None, return None.
    - Recursive step: We use Python's tuple unpacking to simultaneously swap 
      the left and right child pointers while passing the subtrees down into 
      recursive calls.
    - If the input tree is highly unbalanced, an Iterative approach (using a BFS Queue) 
      would be safer to avoid hitting Python's recursion depth limit.
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

if __name__ == '__main__':
    def build_tree(nodes):
        if not nodes: return None
        root = TreeNode(nodes[0])
        queue = [root]
        i = 1
        while queue and i < len(nodes):
            curr = queue.pop(0)
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i])
                queue.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i])
                queue.append(curr.right)
            i += 1
        return root

    def get_level_order(root):
        if not root: return []
        result = []
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr:
                result.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

    sol = Solution()
    t1 = build_tree([4,2,7,1,3,6,9])
    print("Test 1: [4,2,7,1,3,6,9] -> Expected: [4, 7, 2, 9, 6, 3, 1], Got:", get_level_order(sol.invertTree(t1)))
    t2 = build_tree([2,1,3])
    print("Test 2: [2,1,3]         -> Expected: [2, 3, 1], Got:", get_level_order(sol.invertTree(t2)))
    t3 = build_tree([])
    print("Test 3: []              -> Expected: [], Got:", get_level_order(sol.invertTree(t3)))
    print("All tests executed!")
