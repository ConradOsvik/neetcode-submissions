# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

        return self.diameter - 2

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1

        self.diameter = max(left + right, self.diameter)

        print(root.val, left, right)

        return max(left, right)