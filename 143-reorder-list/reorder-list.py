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
            slow = slow.next
            fast = fast.next.next


        prev, curr = None, slow.next
        
        while curr:
            temp, prev, curr = prev, curr, curr.next
            prev.next = temp

        slow.next = None
        currA, currB = head, prev
        while currA and currB:
            tempA, tempB = currA, currB
            currA, currB = currA.next, currB.next
            tempA.next = tempB
            tempB.next = currA



        