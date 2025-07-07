def find(parent, u):
    if parent[u] != u:
        parent[u] = find(parent, parent[u])  # path compression
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    if root_u == root_v:
        return
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = list(range(n))
    rank = [0] * n
    mst_cost = 0
    mst_edges = []

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += w
            mst_edges.append((u, v, w))

    return mst_cost, mst_edges
