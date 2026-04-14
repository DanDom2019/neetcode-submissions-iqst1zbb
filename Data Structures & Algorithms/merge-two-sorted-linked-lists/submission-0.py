# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # dummy head so we always have a node to attach to
        current = dummy         # pointer that walks forward as we build the merged list
        while list1 and list2:                  # loop while BOTH lists have nodes
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next              # advance the list we just consumed
            else:
                current.next = list2
                list2 = list2.next

            current = current.next              # advance the result pointer

        # At most one list still has remaining nodes — attach it directly
        current.next = list1 if list1 else list2

        return dummy.next       # dummy itself isn't part of the answer

            