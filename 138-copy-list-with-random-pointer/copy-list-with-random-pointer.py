class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First Pass: Copy Nodes and Adjust Next Pointers
        curr = head
        while curr:
            temp, curr.next = curr.next, Node(curr.val)
            curr.next.next, curr = temp, temp

        # Second Pass: Adjust Random Pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Third Pass: Separate Original and Copied Lists
        dummy = Node(0)
        curr, copy = head, dummy
        while curr:
            copy.next = curr.next
            curr.next = curr.next.next
            copy = copy.next
            curr = curr.next    

        return dummy.next
        
