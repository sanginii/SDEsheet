#linear search
def BookAllocation(books,n ,m):
    if m > n:
        return -1
    low = max(books)
    high = sum(books)
    for i in range (low,high+1):
        cntStudent=fun(books, i, n)
        if cntStudent==m:
            return i
        
#binary search 
def BinBookAllocation(books,n ,m):
    if m > n:
        return -1
    low = max(books)
    high = sum(books)
    while low<=high:
        mid = (low+high)//2
        cntStudent=fun(books,mid, n) 
        if cntStudent<=m: #I need to increase students
            high = mid-1 #lower half requires more number of students 
        if cntStudent>m: #I need to decrease my number of students
            low = mid+1 #upper half requires less number of students
    return low

#counting number of students
def fun(books, page, n):
    stu=1
    curPage=0
    for i in range(n):
        if curPage+books[i] <= page:
            curPage+=books[i]
        else:
            stu+=1
            curPage=books[i] 
    return stu

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = BinBookAllocation(arr, n, m)
print("The answer is:", ans)