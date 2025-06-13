#bruteforce O(n^2), space O(n)
s = 'bbbbb'
st = set()
mx=0
i=j=l=0
while i < len(s):
    if s[i] not in st:
        st.add(s[i]) 
        l+=1 
        i+=1
    else:
        l=0
        st.clear() 
        j+=1
        i=j
    mx = max(mx,l)
print(mx) 

#optimal sol
#when l is moving we are removing that element from set too 
#sliding window
# Time Complexity: O( 2*N ) (sometimes left and right both have to travel a complete array)
# Space Complexity: O(N) where N is the size of HashSet taken for storing the elements
s = 'abcaabcdba'
st = set ()
l=r=0
mx=0
for r in range(len(s)):
    if s[r] in st:
        while l<r and s[r] in st:
            st.remove(s[l])
            l+=1
    st.add(s[r])
    mx = max(mx,r-l+1)
print (mx) 

#optimal2
# Time Complexity: O(N)
# Space Complexity: O(N) 
s = 'abcaabcdba'
char_index = {}
l = 0
mx = 0

for r in range(len(s)):
    if s[r] in char_index and char_index[s[r]] >= l: #to check if duplicate is in window
        l = char_index[s[r]] + 1
    char_index[s[r]] = r
    mx = max(mx, r - l + 1)

print(mx)
