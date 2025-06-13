# # You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

#XOR METHOD
a = [3,1,2,5,4,6,7,5]
xor = 0
N=len(a)
for i in a:
    xor^=i
for i in range(1,N+1):
    xor^=i
print (xor)
bitno = (xor&-xor).bit_length()-1
print (bitno)
x=0
y=0
for i in a:
    if i>>bitno & 1:
        x^=i
    else:
        y^=i
for i in range(1,N+1):
    if i>>bitno & 1:
        x^=i
    else:
        y^=i
if a.count(x)==2:
    A=x
    B=y
else:
    A=y
    B=x
print("a =", A, "b =", B) 


#BRUTEFORCE O(n^2)
a = [3,1,2,5,3]
l = len(a)
expsum = (l*(l+1))//2
for i in range (l):
    for j in range (i,l):
        if a[i]==a[j]:
            A=a[i]

# better 
#sort first O(nlogn)
b=sorted(a)
for i in range (l-1):
    if b[i]==b[i+1]:
        A=b[i] 

#better space complexity O(n) time O(n)
freq = {}
N=len(a)
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1 
for i in range (i,N+1):
    if i in freq:
        if freq[i]==2:
            A=i
    else:
        B=i

print ("a =",A,"b =",B) 

# better O(n) time O(n) space
#how to find duplicate element in list in linear time 
a = [3,1,2,5,4,6,7,5]
l = len(a)
expsum = (l*(l+1))//2
seen = set()
duplicate = set()
for i in a:
    if i in seen:
        A=i
        break
    else:
        seen.add(i) 
B=expsum-sum(a)+A
print ("a =",A,"b =",B)  

#Optimal O(n) space O(1) math solution
a = [3, 1, 2, 5, 3]
N = len(a)

sum_actual = sum(a)
sum_expected = (N * (N + 1)) // 2

sum_squares_actual = sum(x * x for x in a)
sum_squares_expected = (N * (N + 1) * (2 * N + 1)) // 6

diff = sum_actual - sum_expected           # A - B
square_diff = sum_squares_actual - sum_squares_expected  # A² - B²

# From (A² - B²) = (A - B)(A + B)
sum_ab = square_diff // diff               # A + B

A = (diff + sum_ab) // 2
B = sum_ab - A

print("a =", A, "b =", B)




