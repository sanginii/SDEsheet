N = 10
nums = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
# freq = {}
# for i in nums:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# if max(freq.values()) > N/2:
#     print (max(freq, key=freq.get))

#optimal

count=0
for i in range(len(nums)):
    if count==0:
        ele = nums[i]
    if nums[i]==ele:
        count+=1
    else:
        count-=1
count=0
for i in nums:
    if i==ele:
        count+=1
if count>N/2:
    print(ele)
    
