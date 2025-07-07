def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    # Initialize distances
    for u in range(n):
        dist[u][u] = 0
        for v, w in graph[u]:
            dist[u][v] = w

    # Main DP loop
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
