# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        half, slow, fast = slow, None, slow.next
        half.next = None
        while fast:
            temp, slow, fast = slow, fast, fast.next
            slow.next = temp
        a, b = head, slow
        while a and b:
            temp1, temp2 = a.next, b.next
            a.next = b
            b.next = temp1
            a, b = temp1, temp2
        return head
