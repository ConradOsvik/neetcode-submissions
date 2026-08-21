# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Deque, Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue: Deque[Optional[TreeNode]] = deque()
        queue.append(p)
        queue.append(q)

        while len(queue) > 0:
            p = queue.pop()
            q = queue.pop()

            if p and not q:
                return False
            if q and not p:
                return False

            if p and q:
                if p.val != q.val:
                    return False

                queue.append(p.left)
                queue.append(q.left)
                queue.append(p.right)
                queue.append(q.right)

        return True
