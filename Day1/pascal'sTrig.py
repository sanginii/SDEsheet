#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1

#variation 1
r=5
c=4
#r-1Cc-1 formula
r=r-1
c=c-1
res=1
for i in range (c):
        res=res*(r-i)
        res=res/(i+1)
print (int(res))

#variation 2
n=3
a = [1]
ans=1
for i in range (1,n):
     ans = ans * (n-i)
     ans = ans / i
     a.append(int(ans))
print (a)

#variation 3 
n=5
a = [[0] * (i+1) for i in range(n)] 
for i in range (0,n):
    a[i][0]=1
    for j in range (1, i+1):
        if j<i:
            a[i][j]=a[i-1][j]+a[i-1][j-1] 
        else:
            a[i][j]=1

for i in range(n):
    print(' ' * (n - i), end=' ')
    for j in a[i]:
        print(j, end=' ')
    print() 