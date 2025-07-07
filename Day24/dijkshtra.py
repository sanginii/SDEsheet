import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue  # already processed with shorter distance

        for v, w in graph[u]:  # (neighbor, weight)
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist
