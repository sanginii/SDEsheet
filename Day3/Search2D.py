# def search1(N, M, target, mat):
#     flag = 0 
#     for row in mat:
#         if row[M-1] >= target:
#             flag = 1
#             break 
#     if flag == 0:
#         return(False)
#     else:
#         low=0
#         high=M
#         # use binary search to find the ele in row
#         while (low<high):
#             mid = (low+high)//2
#             if target==mid:
#                 return (True)
#             elif target > mid:
#                 low=mid+1
#             else:
#                 high=mid-1
#         return (False)

#optimal
def search(N, M, target, mat):
    low=0
    high=N*M-1
    while (low<=high):
        mid = (low+high)//2
        row = mid//M 
        col = mid%M
        if mat[row][col]==target:
            return (True)
        elif mat[row][col]<target:
            low=mid+1
        else:
            high=mid-1
    return (False) 

N = 3
M = 3
target = 11
mat = [[1, 2, 4], [6, 7, 8], [9, 10, 34]]
print (search(N,M,target,mat)) 