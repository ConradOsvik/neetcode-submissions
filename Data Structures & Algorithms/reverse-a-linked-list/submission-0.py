# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            if not prev:
                tail = ListNode(curr.val)
                prev = tail
            else:
                node = ListNode(curr.val, prev)
                prev = node

            if curr.next:
                curr = curr.next
            else:
                curr = None

        return prev