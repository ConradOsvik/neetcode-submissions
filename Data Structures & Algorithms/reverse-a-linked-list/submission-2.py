# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            if not prev:
                prev = head
                head = head.next
                prev.next = None
                continue

            print(head.val, prev.val)

            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev
            