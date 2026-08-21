# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head or head.next:
        #     return False

        curr = head

        while curr:
            if not curr.next:
                return False

            if not curr.val:
                return True
            
            curr.val = None

            curr = curr.next

        return False