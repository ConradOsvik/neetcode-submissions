# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and not head.next:
            return

        slow = head
        fast = head

        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        end = None
        while slow:
            if not end:
                end = slow
                slow = slow.next
                end.next = None

            temp = slow.next
            slow.next = end
            end = slow
            slow = temp

        prev = None
        while end:
            if not head:
                break

            temp = head.next
            temp2 = end.next
            head.next = end
            end.next = temp
            head = temp
            prev = end
            end = temp2

        prev.next = end
