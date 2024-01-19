# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first pass: calculate length to determine number of k groups
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        # second pass: reverse one k group at a time and join it to previous tail
        dummy = ListNode()
        curr, tail = head, dummy
        for _ in range(n // k):
            new_tail, prev = curr, None
            for _ in range(k):
                temp, prev, curr = prev, curr, curr.next
                prev.next = temp
            tail.next = prev
            tail = new_tail
        
        # if left-out nodes, join them to the tail
        if curr:
            tail.next = curr
        
        return dummy.next
            
