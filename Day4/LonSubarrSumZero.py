#optimal solution is storing the previous prefix sums similar to dp and updating if new max found
# in subarrray problems when we need previous vales too  use dp
a=[9, -3, 3, -9, 10, -10] 
N=len(a)
sum=cnt=0
mx=float("-inf")
prefix = {}
for i in range (N):
    sum+=a[i]
    if sum==0:
        cnt=i+1
    elif sum not in prefix:
        prefix[sum]=i
    else:
        cnt=i-prefix[sum]
    mx = max(mx,cnt)
print(mx)
    
