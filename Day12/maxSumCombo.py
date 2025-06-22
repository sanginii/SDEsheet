import heapq
A = [1, 4, 2, 3]
B = [2, 5, 1, 6] 
N = 4
K = 4
A.sort(reverse=True)
B.sort(reverse=True) 
max_heap = []
heapq.heappush(max_heap,(-(A[0]+B[0]),0,0))
visited = set()
visited.add((0,0))
i=j=0
res = []
while K > 0:
    current_sum, i, j = heapq.heappop(max_heap)
    res.append(-current_sum)
    if i+1<N and (i+1,j) not in visited:
        heapq.heappush(max_heap,(-(A[i+1]+B[j]),i+1,j)) 
        visited.add((i+1,j))
    if j+1<N and (i,j+1) not in visited:
        heapq.heappush(max_heap,(-(A[i]+B[j+1]),i,j+1)) 
        visited.add((i,j+1)) 
    K-=1 
print(res) 