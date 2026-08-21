# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l1
        rest = 0
        prev = None
        while l1 or l2:
            total = rest
            if l1:
                total += l1.val
            if l2:
                total += l2.val

            rest, val = divmod(total, 10)

            print(rest, val)

            if l1:
                l1.val = val
                prev = l1
            elif l2:
                if prev:
                    prev.next = l2
                prev = l2
                l2.val = val

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if rest:
            prev.next = ListNode(rest)
            
        return dummy