def merge_sort(a):
    if (len(a)>1):
        mid = len(a)//2
        b=a[:mid]
        c=a[mid:]
        count = merge_sort(b) + merge_sort(c)
        l=m=0
        while l<len(b):
            while m<len(c) and b[l]>2*c[m]:
                m+=1
            l+=1
            count+=m 
        merge(b,c,a) 
        return (count)
    else:
        return 0
       
def merge(b,c,a):
    i=j=k=0
    while i<len(b) and j<len(c):
        if b[i]<c[j]:
            a[k]=b[i]
            i+=1
        else:
            a[k]=c[j] 
            j+=1
        k+=1
    while i<len(b):
        a[k]=b[i]
        i+=1
        k+=1
    while j<len(c):
        a[k]=c[j]
        j+=1
        k+=1
a=[2,4,3,5,1]
print (merge_sort(a)) 
