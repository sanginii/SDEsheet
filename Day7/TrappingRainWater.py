#bruteforce O(N^2)
h = [4,2,0,3,2,5]
def maxleft(idx):
    max = 0
    for i in range(idx):
        if h[i]>max:
            max = h[i]
    return max
def maxright(idx):
    max=0
    for i in range(idx+1,len(h)):
        if h[i]>max:
            max = h[i]
    return max
ans=0
for i in range(1,len(h)-1):
    trapwat = min(maxleft(i),maxright(i))-h[i]
    ans+= trapwat if trapwat > 0 else 0
print (ans)

#better by taking prefix suffix sum time - O(3N) Space - O(2N)
def trap(arr):
    n = len(arr)
    prefix = [0] * n
    suffix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], arr[i])
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], arr[i])
    waterTrapped = 0
    for i in range(n):
        waterTrapped += min(prefix[i], suffix[i]) - arr[i]
    return waterTrapped 