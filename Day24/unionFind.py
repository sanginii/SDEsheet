# Initialization
parent = [i for i in range(n)]
rank = [0] * n

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])  # Path Compression
    return parent[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u == root_v:
        return  # already in the same set

    # Union by Rank
    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1
