import heapq
arr = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]
k = 3 
res = [] 
i = 0
heap = []
while i < k :
    heapq.heappush(heap, (arr[i][0], i, 0)) 
    i+=1
while heap:
    val, arrind, eleind = heapq.heappop(heap) 
    res.append(val)
    if eleind+1 < len(arr[arrind]):
        heapq.heappush(heap, (arr[arrind][eleind+1], arrind, eleind+1))  
print (res) 

#push pop log k (N times)