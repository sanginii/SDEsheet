def topological_sort_dfs(n, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * n
    result = []
    on_path = [False] * n  # optional, for cycle detection

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return result[::-1]  # reverse to get topological order
