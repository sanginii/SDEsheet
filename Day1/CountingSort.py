a = [2,0,2,1,1,0] 
low=mid=0
high=len(a)-1
while mid<high:
    if a[mid]==0:
        a[low],a[mid]=a[mid],a[low]
        low+=1
        mid+=1
    if a[mid]==1:
        mid+=1
    if a[mid]==2:
        a[high],a[mid]=a[mid],a[high]
        high-=1
print (a) 