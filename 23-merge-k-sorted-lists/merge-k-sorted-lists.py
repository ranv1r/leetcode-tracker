# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge(l1, l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val > l2.val:
                    l1, l2 = l2, l1
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next
        while len(lists) > 1:
            new_lists = [] 
            i = 0
            while i < len(lists):
                new_list = merge(lists[i], lists[i + 1]) if i + 1 < len(lists) else lists[i]
                new_lists.append(new_list)
                i += 2
            lists = new_lists
        return lists.pop()