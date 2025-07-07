def has_cycle_dfs_directed(graph, n):
    visited = [False] * n
    rec_stack = [False] * n  # recursion stack

    def dfs(node):
        visited[node] = True
        rec_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:
                return True  # Cycle detected

        rec_stack[node] = False
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True
    return False
