"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/trees/invert_tree.py until you're done.

Problem (Invert Binary Tree, LeetCode 226):

Given the root of a binary tree, invert it (mirror every node's left
and right children) and return the new root.

Example:
      4                4
    /   \            /   \
   2     7    ->    7     2
  / \   / \        / \   / \
 1   3 6   9      9   6 3   1

Write your solution below (recursive DFS).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return

        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

    def inverttreeit(self, root):
        if not root:
            return

        stack = [root]
        cur = root

        while stack:
            cur = stack.pop()
            cur.right, cur.left = cur.left, cur.right
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        return root



if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
