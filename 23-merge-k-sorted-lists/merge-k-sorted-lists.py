# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.mergeLists(lists)

    def mergeLists(self, lists):
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        half = len(lists) // 2
        leftHalf, rightHalf = lists[:half], lists[half:]

        return self.mergeTwoLists(
            self.mergeLists(leftHalf), 
            self.mergeLists(rightHalf)
        )
        

    def mergeTwoLists(self, node1, node2):
        dummy = ListNode()
        res = dummy
        while node1 and node2:
            node1, node2 = (node1, node2) if node1.val <= node2.val else (node2, node1)
            res.next = node1
            node1 = node1.next
            res = res.next
        if node1:
            res.next = node1
        if node2:
            res.next = node2
        return dummy.next
            