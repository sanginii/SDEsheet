from collections import defaultdict
def prmut(nums):
    def help(nums, mpp, ans, lst):   
        if len(lst)==len(nums):
            ans.append(list(lst))
            return
        for i in range (len(nums)):
            if nums[i] not in mpp or mpp[nums[i]]==0:
                mpp[nums[i]] = 1
                lst.append(nums[i])
                help(nums, mpp, ans, lst) 
                lst.pop()
                mpp[nums[i]] = 0
    ans = []
    mpp = {}
    help(nums, mpp, ans, [])
    return (ans)
nums = [1,2,3] 
print (prmut(nums)) 