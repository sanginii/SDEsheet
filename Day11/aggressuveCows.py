N = 5 #stalls
k = 2 #cows
arr = [4,2,1,3,6] 
def distance(n, k, arr):
    arr.sort()
    low = 1
    high = arr[-1]-arr[0] 
    while low<=high:
        mid = (low+high)//2
        noOfcows = cowno(mid,arr)
        if noOfcows < k: #increase cows
            high = mid-1
        if noOfcows >= k:
            low = mid+1
    return high

def cowno(dis, arr):
    cows = 1
    last_pos = arr[0]
    for i in range(1,len(arr)):
        if arr[i]-last_pos>=dis:
            cows+=1 
            last_pos = arr[i]
    return cows
print (distance(N, k, arr)) 