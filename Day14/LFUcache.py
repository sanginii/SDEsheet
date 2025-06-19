class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLL:  # Doubly Linked List for each frequency
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self):
        if self.tail.prev == self.head:
            return None
        last = self.tail.prev
        self.remove(last)
        return last

    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_node = {}
        self.freq_map = {}
        self.min_freq = 0

    def _update(self, node):
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].is_empty():
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1
        self.freq_map.setdefault(node.freq, DLL()).add(node)

    def get(self, key):
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.key_node:
            node = self.key_node[key]
            node.val = value
            self._update(node)
        else:
            if len(self.key_node) == self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                to_remove = lfu_list.remove_last()
                del self.key_node[to_remove.key]

            new_node = Node(key, value)
            self.key_node[key] = new_node
            self.freq_map.setdefault(1, DLL()).add(new_node)
            self.min_freq = 1
