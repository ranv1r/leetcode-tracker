class ListNode:
    def __init__(self, key = 0, value = 0, next_node = None, prev_node = None):
        self.key = key
        self.value = value
        self.next = next_node
        self.prev = prev_node

class LRUCache:
    """
    Stores key-value pairs. An integer key is mapped to a Double-linked list node using a dictionary.
    """

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.capacity = capacity
        self.left = ListNode() # left is least recently used
        self.right = ListNode() # right is most recently used
        
        # Setting up empty linked list with two dummy nodes on edges
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        l, r = node.prev, node.next
        l.next = r
        r.prev = l
    
    def push(self, node):
        l, r = self.right.prev, self.right
        l.next = node
        node.prev = l
        node.next = r
        r.prev = node
    
    def evict(self):
        key = self.left.next.key
        del self.cache_dict[key]
        self.remove(self.left.next)

    def get(self, key: int) -> int:
        # look up cache_dict for key
        result = self.cache_dict.get(key, -1)
        # if not exists return -1
        if result == -1:
            return result
        # remove from linked list
        self.remove(result)
        # add to right edge of linked list
        self.push(result)
        return result.value
        

    def put(self, key: int, value: int) -> None:
        # case 1: key already exists
        if key in self.cache_dict:
            result = self.cache_dict[key]
            # remove from list
            self.remove(result)
            # update value
            result.value = value
            # add to list right edge
            self.push(result)
        # case 2: key does not exist
        else:
            # add to the right edge of the list
            new_node = ListNode(key, value)
            self.push(new_node)
            self.cache_dict[key] = new_node
            # if new size exceeds capacity
            if len(self.cache_dict) > self.capacity:
                # evict element from left edge
                self.evict()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)