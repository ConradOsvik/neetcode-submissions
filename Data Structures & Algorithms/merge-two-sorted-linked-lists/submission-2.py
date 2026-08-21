# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
    
        head = None
        tail = None

        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode(list1.val, None)

                if not head:
                    head = node

                if not tail:
                    tail = node
                else:
                    tail.next = node
                    tail = node
                
                list1 = list1.next
            else:
                node = ListNode(list2.val, None)

                if not head:
                    head = node

                if not tail:
                    tail = node
                else:
                    tail.next = node
                    tail = node

                list2 = list2.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return head

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1

#         tail = ListNode(list2.val, None) if list1.val <= list2.val else ListNode(list1.val, None)
#         head = ListNode(list1.val, tail) if list1.val <= list2.val else ListNode(list2.val, tail)
#         curr1 = list1.next
#         curr2 = list2.next

#         while curr1 and curr2:
#             if curr1.val <= curr2.val:
#                 node2 = ListNode(curr2.val, None)
#                 node1 = ListNode(curr1.val, node2)
#                 tail.next = node1
#                 tail = node2
#             else:
#                 node1 = ListNode(curr1.val, None)
#                 node2 = ListNode(curr2.val, node1)
#                 tail.next = node2
#                 tail = node1

#             print(curr1.val, curr2.val)
#             curr1 = curr1.next
#             curr2 = curr2.next

#         if curr1 and curr1.next:
#             tail.next = curr1
#         if curr2 and curr2.next:
#             tail.next = curr2
    
#         return head

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1

#         tail = ListNode(list2.val, None) if list1.val <= list2.val else ListNode(list1.val, None)
#         head = ListNode(list1.val, tail) if list1.val <= list2.val else ListNode(list2.val, tail)
#         curr1 = list1.next
#         curr2 = list2.next

#         while curr1 and curr1.next and curr2 and curr2.next:
#             node1 = curr1
#             node2 = curr2
#             if node1.val <= node2.val:
#                 node2.next = None
#                 node1.next = node2
#                 tail.next = node1
#                 tail = node2
#             else:
#                 node1.next = None
#                 node2.next = node1
#                 tail.next = node2
#                 tail = node1

#             print(curr1.val, curr1.next.val)

#             curr1 = curr1.next
#             curr2 = curr2.next

#             print(curr1.val, curr1.next.val if curr1.next else None)

#         if list1.next:
#             tail.next = list1
#         if list2.next:
#             tail.next = list2
    
#         return head

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1:
#             return list2
#         if not list2:
#             return list1

#         curr1 = list1
#         curr2 = list2
#         head = None
#         tail = None

#         if curr1.val <= curr2.val:
#             node1 = ListNode(curr1.val, curr2)
#             node2 = ListNode(curr2.val, None)
#             head = node1
#             tail = node2
#         else:
#             node1 = ListNode(curr2.val, curr1)
#             node2 = ListNode(curr1.val, None)
#             head = node1
#             tail = node2

#         while curr1.next and curr2.next:
#             if curr1.next.val <= curr2.next.val:
#                 node1 = ListNode(curr1.val, curr2)
#                 node2 = ListNode(curr2.val, None)
#                 tail.next = node1
#                 tail = node2
#             else:
#                 node1 = ListNode(curr2.val, curr1)
#                 node2 = ListNode(curr1.val, None)
#                 tail.next = node1
#                 tail = node2

#             curr1 = curr1.next
#             curr2 = curr2.next

#         if curr1.next:
#             tail.next = curr1.next
#         if curr2.next:
#             tail.next = curr2.next
    
#         return head