prices=[1, 0, 1, 1, 0, 1]
cnt=0
mx = float("-inf")
for i in prices:
    if i==1:
        cnt+=1
        mx = max(mx,cnt)
    else: 
        cnt=0
print(mx) 