class Node:
    def __init__ (self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def add(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node 
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val 
    
    def put (self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.add(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                del self.cache[lru.key]
                self.remove(lru)     
            node = Node(key, value)
            self.cache[key] = node
            self.add(node)

#space complexity is O(capacity) for nodes and storing nodes in mapp

          

    
    
    