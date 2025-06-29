from collections import deque
def MaxofMinWindSize(arr):
    n = len(arr)
    ans = []
    for k in range (1,n+1): 
        que = deque ()
        mx = float("-inf")
        for i in range(n):
            while que and arr[que[-1]] >= arr[i]:
                que.pop()
            que.append(i)
            if que[0] <= i - k:
                que.popleft()
            if i >= k - 1: #one full window
                mx = max(mx, arr[que[0]])
        ans.append(mx)
    return ans
arr = [10,20,30,50,10,70,30]
print (MaxofMinWindSize(arr)) 
#bruteforce O(n^2)