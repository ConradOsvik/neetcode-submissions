# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left and (root.left.left or root.left.right):
                self.invertTree(root.left)
            
            if root.right and (root.right.left or root.right.right):
                self.invertTree(root.right)

            if root.left or root.right:
                temp = root.left
                root.left = root.right
                root.right = temp

        return root