a = [[1,2,3],[4,5,6],[7,8,9]]
m = len(a)
n = len(a[0])
deg=180
k=(deg%360)//90
for _ in range (k):
    for i in range (m):
        for j in range (n):
            if j>i:
                a[i][j],a[j][i]=a[j][i],a[i][j]
    for i in range(m):
        a[i].reverse()
print (a) 