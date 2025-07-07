from collections import defaultdict, deque

def topological_sort_bfs(n, edges):
    graph = defaultdict(list)
    in_degree = [0] * n

    # Step 1: Build graph and in-degree array
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Step 2: Initialize queue with nodes having in-degree 0
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    # Step 3: Process nodes
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all nodes are in result, return it; else, return empty (cycle detected)
    return result if len(result) == n else []
