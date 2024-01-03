# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev, curr = dummy, head
        while curr:
            temp = curr
            headNextk, curr, n = self.reverseNextK(curr, k)
            if n < k:
                headNextk, curr, _ = self.reverseNextK(headNextk, k)
            prev.next = headNextk
            prev = temp
        return dummy.next

    def reverseNextK(self, curr, k):
        """Return the (head of reversed next k, next pointer, length of reversed segment)
        """
        prev = None
        n = 0
        for i in range(1, k + 1):
            if not curr:
                break
            n = i
            temp, prev, curr = prev, curr, curr.next
            prev.next = temp
        return prev, curr, n

