candidates = [10, 1, 2, 7, 6, 1, 5]
candidates.sort()  # sort to handle duplicates
target = 8
ans = []

def combtwo(ind, lst, target):
    if target == 0:
        ans.append(lst[:])
        return
    for i in range(ind, len(candidates)):
        # Skip duplicates
        if i > ind and candidates[i] == candidates[i - 1]:
            continue
        # If candidate exceeds target, break (since sorted)
        if candidates[i] > target:
            break
        lst.append(candidates[i])
        combtwo(i + 1, lst, target - candidates[i])  # i+1: use only once
        lst.pop()

combtwo(0, [], target)
print(ans) 