# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.sub = []
        self.isSub = False
        def dfs_sub(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return []

            left = dfs_sub(root.left)
            right = dfs_sub(root.right)

            return [root.val, *left, *right]

        self.sub = dfs_sub(subRoot)
        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return []

            left = dfs(root.left)
            right = dfs(root.right)

            arr = [root.val, *left, *right]

            if arr == self.sub:
                self.isSub = True

            return arr

        dfs(root)

        return self.isSub