def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)
    print(node)  # process the node
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)

# Usage:
graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 3]
}
visited = set()
dfs(1, graph, visited)
