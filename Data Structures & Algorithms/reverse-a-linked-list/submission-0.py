class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            next = curr.next    # 1. save next before you lose it
            curr.next = prev    # 2. flip the arrow ←
            prev = curr         # 3. move prev forward
            curr = next         # 4. move curr forward
        return prev