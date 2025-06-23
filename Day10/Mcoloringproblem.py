from  collections import defaultdict
#dfs style instead of bfs
def mcoloring(n, m, adj, color, v):
    if v == n:
        return True
    for c in range(m):
        if all(color[neighbor] != c for neighbor in adj[v]):
            color[v] = c  # Assign color
            if mcoloring(n, m, adj, color, v + 1):
                return True
            color[v] = -1 
    # If no color can be assigned to v, return False  
    return False 

# Inputs
n = 4
m = 3
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 2)
]

# Build adjacency list
adj = defaultdict(list)
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

# Start coloring
color = [-1] * n
if mcoloring(n, m, adj, color, 0):
    print("1 (Coloring possible)")
else:
    print("0 (Coloring not possible)") 