# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        half = end = head
        # find halfway point
        while end.next and end.next.next:
            half = half.next
            end = end.next.next

        # split lists and reverse part2
        prev, curr, half.next = None, half.next, None
        while curr:
            temp, prev, curr = prev, curr, curr.next
            prev.next = temp
        # interleave lists
        while prev:
            temp1, temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2

        