A = [3,10,4,2,1,2,6,1,7,2,9] 
l = len(A)
res = [-1]*l
st = [] 
for i in range (2*l-1,-1,-1):
    while st and A[i%l]<=st[-1]:
        st.pop()
    if i<l:
        if st:
            res[i%l]=st[-1] 
    st.append(A[i%l])    
print (res)
    