ans = []
arr = [3, 1, 2]
n = len(arr)
def subsetSums(ind: int, sum: int):
    if ind == n:
        ans.append(sum)
        return
    # element is picked
    subsetSums(ind + 1, sum + arr[ind])
    # element is not picked
    subsetSums(ind + 1, sum) 
subsetSums(0, 0)
ans.sort()
print (ans) 