ans = []
ds = []
candidates = [2, 3, 6, 7]
target = 7

def findCombination(ind: int, target: int):
    if ind == len(candidates):
        if target == 0:
            ans.append(ds[:])
        return
    if candidates[ind] <= target:
        ds.append(candidates[ind])
        findCombination(ind, target - candidates[ind])
        ds.pop()
    findCombination(ind + 1, target)
    
findCombination(0, target)
print (ans) 