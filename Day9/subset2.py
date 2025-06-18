nums = [1,2,2]
ans = []
res = set()
def subsetsum2(ds, index):
    if index==len(nums):
        ds.sort()
        res.add(tuple(ds))
        return
    ds.append(nums[index])
    subsetsum2(ds, index+1)
    ds.pop()  
    subsetsum2(ds, index+1) 
subsetsum2([],0)
for it in res:
    ans.append(list(it))
print (ans)