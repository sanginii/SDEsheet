#remove duplicate from sorted array
#bruteforce
a = [3,3,3,5,5,6,7]
l = len(a)
i=0
while i < (l-1):
    if a[i]==a[i+1]:
        for j in range (i+1,l-1):
            a[j]=a[j+1]
        l-=1
    else:
        i+=1
print (len(a[:l])) 

#better
result = []
for i in a:
    if not result or result[-1]!=i:
        result.append(i)
print (result) 

#optimal
nums = [3,3,3,5,5,6,7]
i=0
j=1
while j < len(nums):
    if nums[i]!=nums[j]:
        i+=1
        nums[i]=nums[j] 
    j+=1
print ((nums[:i+1]))
