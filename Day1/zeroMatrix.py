#optimal
matrix = [[1,1,1],[1,0,1],[1,1,1]] 
m=len(matrix)
n=len(matrix[0]) 
col1=1
for i in range (m):
    for j in range (n):
        if matrix [i][j]==0:
            if j==0:    
                col1=0
            else: 
                matrix[0][j]=0 
            matrix[i][0]=0

for i in range(1,m):
    if matrix[i][0]==0:
        for k in range (n):
            matrix[i][k]=0
for j in range(1,n):
    if matrix[0][j]==0:
        for k in range (m):
            matrix[k][j]=0

if matrix[0][0]==0:
    for k in range (n):
        matrix[0][k]=0
if col1==0:
    for k in range (m):
        matrix[k][0]=0
print (matrix)


#bruteforce
for i in range (m):
    for j in range (n):
        if matrix [i][j]==0:
            for k in range (n):
                if matrix [i][k]!=0:
                    matrix[i][k]=-1
            for k in range (m):
                if matrix [k][j]!=0:
                    matrix[k][j]=-1
for i in range (m):
    for j in range (n):
        if matrix [i][j]==-1:
            matrix [i][j]=0


#better
r = [0]*m
c = [0]*n
for i in range (m):
    for j in range (n):
        if matrix [i][j]==0:
            r[i]=1
            c[j]=1
for i in range(m):
    if r[i]==1:
        for k in range (n):
            matrix[i][k]=0
for j in range(n):
    if c[j]==1:
        for k in range (m):
            matrix[k][j]=0
print (matrix) 

