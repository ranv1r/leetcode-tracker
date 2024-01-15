"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            temp, curr.next = curr.next, Node(curr.val)
            curr.next.next, curr = temp, temp

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        dummy = Node(0)
        curr, copy = head, dummy
        while curr:
            copy.next = curr.next
            curr.next = curr.next.next
            copy = copy.next
            curr = curr.next    
    
        return dummy.next
        
