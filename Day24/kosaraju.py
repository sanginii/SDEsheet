from collections import defaultdict

def kosaraju_scc(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [False] * n
    stack = []

    # Step 1: DFS to fill stack with finishing times
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        stack.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # Step 2: Transpose the graph
    transpose = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            transpose[v].append(u)

    # Step 3: DFS on transposed graph
    visited = [False] * n
    sccs = []

    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in transpose[u]:
            if not visited[v]:
                dfs2(v, component)

    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs2(u, component)
            sccs.append(component)

    return sccs
