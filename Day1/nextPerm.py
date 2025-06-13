#O(n) time complexity
a = [1,4,3,2]
i = len(a)-2
while i >=0 and a[i]>=a[i+1]:
    i-=1
if i == -1:
     a.reverse()
else:
    j=len(a)-1
    while a[j]<=a[i]:
        j-=1
    a[i],a[j]=a[j],a[i]
    a[i+1:]=reversed(a[i + 1:])
print (a) 
    