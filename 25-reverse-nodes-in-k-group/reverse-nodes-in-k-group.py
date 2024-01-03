class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        prev, curr = None, head
        # reverse first k group
        for _ in range(k):
            temp, prev, curr = prev, curr, curr.next
            prev.next = temp
        # recursively reverse rest of valid k group
        head.next = self.reverseKGroup(curr, k)
        return prev
