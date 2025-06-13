arr=[900,940,950,1100,1500,1800]
dep=[910,1200,1120,1130,1900,2000]
arr.sort()
dep.sort()
ans = 1
count = 1
i = 1
j = 0
while i < len(arr) and j < len(dep):
    if arr[i] <= dep[j]:  # one more platform needed
        count += 1
        i += 1
    else:  # one platform can be reduced
        count -= 1
        j += 1
    ans = max(ans, count)  # updating the value with the current maximum
print (ans)
