# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        def dfs(root: Optional[TreeNode], low, high):
            if not root:
                return

            if not low < root.val < high:
                self.isValid = False

            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            return

        dfs(root, -math.inf, math.inf)

        return self.isValid