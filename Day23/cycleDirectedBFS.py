from collections import defaultdict, deque

def has_cycle_bfs_directed(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n

    # Step 1: Build graph and in-degree array
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Step 2: Initialize queue with all nodes having in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    count = 0

    # Step 3: Process nodes
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If not all nodes were processed → cycle
    return count != n
