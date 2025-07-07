def bellman_ford(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return "Negative cycle detected"

    return dist
