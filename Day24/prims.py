import heapq

def prims_mst(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)
    mst_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return mst_cost
