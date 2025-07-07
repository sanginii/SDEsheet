from collections import deque

def has_cycle_bfs(graph):
    visited = set()

    for start in graph:
        if start in visited:
            continue

        queue = deque()
        queue.append((start, -1))  # (node, parent)
        visited.add(start)

        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    # visited neighbor that's not parent = cycle
                    return True

    return False
