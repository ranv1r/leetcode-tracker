# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [node for node in lists if node]
        lists.sort(key=lambda node: node.val, reverse=True)
        head = curr = ListNode()
        while lists:
            smallest_node = lists.pop()
            if not smallest_node:
                continue
            curr.next = smallest_node
            curr = curr.next
            node, curr.next = curr.next, None
            if node:
                i = 0
                while i < len(lists) and lists[i].val > node.val:
                    i += 1
                lists.insert(i, node)
        return head.next


