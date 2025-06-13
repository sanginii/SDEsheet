a = [-2,1,-3,4,-1,2,1,-5,4] 
maxsum=float("-inf")
sum=0
i=j=k=0
for idx in range (len(a)):
    sum+=a[idx] 
    if maxsum<sum:
        maxsum=sum
        i=k 
        j=idx 
    if sum<0:
        sum=0
        k = idx + 1

print (maxsum)
print (a[i:j+1]) 

#for more than one subarray with maximum sum
results = []  # list to store (start, end) of all max subarrays

for idx in range(len(a)):
    currsum += a[idx]

    if currsum > maxsum:
        maxsum = currsum
        results = [(k, idx)]  # new max, reset list

    elif currsum == maxsum:
        results.append((k, idx))  # same max, add to list

    if currsum < 0:
        currsum = 0
        k = idx + 1

print("Max Sum:", maxsum)
print("All Subarrays with Max Sum:")
for start, end in results:
    print(a[start:end+1])