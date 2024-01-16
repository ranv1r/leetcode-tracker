class Node:
    def __init__(self, key = 0, next = None, prev = None):
        self.key = key # (key, val) tuple
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.mru = Node() # Most Recently Used
        self.lru = Node() # Least Recently Used
        self.lru.next = self.mru
        self.mru.prev = self.lru
        self.cache = {}
        self.cap = capacity

    def insert(self, node):
        left, right = self.mru.prev, self.mru
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right
    
    def delete(self, node):
        left, right =  node.prev, node.next
        left.next = right
        right.prev = left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node, value = self.cache[key]
        self.delete(node)
        self.insert(node)
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node, _ = self.cache[key]
            self.delete(node)
        else:
            node = Node(key)
        self.insert(node)
        self.cache[key] = (node, value)
        if len(self.cache) > self.cap:
            del self.cache[self.lru.next.key]
            self.delete(self.lru.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)