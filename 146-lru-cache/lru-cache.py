class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # stores {key: node ref}
        self.right, self.left = Node(0, -1), Node(0, -1)
        self.right.prev, self.left.next = self.left, self.right

    def insert(self, node):
            temp = self.right.prev
            temp.next = node
            node.prev = temp
            node.next = self.right
            self.right.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        return self.cache.get(key, Node(0, -1)).val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        print(len(self.cache))
        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)