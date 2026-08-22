# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def popNode(queue):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            return node
        
        if not root:
            return []
        
        queue = deque([root])
        ans = []

        while queue:
            l = len(queue)

            for _ in range(l - 1):
                popNode(queue)
            
            node = popNode(queue)
            ans.append(node.val)

        return ans