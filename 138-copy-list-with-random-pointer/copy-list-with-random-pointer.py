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
        dummy = Node(0)
        copy = dummy
        curr = head
        copies = {}
        while curr:
            temp = Node(curr.val)
            copy.next = temp
            copy = temp
            copies[curr] = copy
            curr = curr.next
        
        curr = head
        copy = dummy.next
        while curr:
            if curr.random:
                
                copy.random = copies[curr.random]

            copy = copy.next
            curr = curr.next
        
        return dummy.next
        
