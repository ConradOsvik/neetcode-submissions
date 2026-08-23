# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            dfs(root.left)
            self.nodes.append(root.val)
            dfs(root.right)

        dfs(root)

        for _ in range(k - 1):
            self.nodes.pop(0)

        return self.nodes[0]