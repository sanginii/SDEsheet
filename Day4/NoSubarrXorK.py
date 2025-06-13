a = [4, 2, 2, 6, 4] 
k = 6
n = len(a) # size of the given array.
xr = 0
mpp = {} 
mpp[xr] = 1 # setting the value of 0.
cnt = 0 
for i in range(n):
    xr = xr ^ a[i]
    x = xr ^ k
    if x in mpp:
        cnt += mpp[x]
    if xr in mpp:
        mpp[xr] += 1
    else:
        mpp[xr] = 1 
print (cnt) 