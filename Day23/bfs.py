from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node.val)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Usage:
# bfs(start_node)
