# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.node = root

        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                self.node = root

            if root == p and (left or right):
                self.node = root
            if root == q and (left or right):
                self.node = root

            if root == p:
                return True
            if root == q:
                return True

            return True if (left or right) else False

        dfs(root)

        return self.node