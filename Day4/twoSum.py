#better O(n) time, O(n) space
def two_sum(arr, target):
    seen = {}  # value: index
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return [-1, -1]

#optimal O(n log n) time, O(n) space if asked to not use map
def two_sum_two_pointers(arr, target):
    nums = [(val, idx) for idx, val in enumerate(arr)]
    # Result: [(2, 0), (6, 1), (5, 2), (9, 3)]
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l][0] + nums[r][0]
        if s == target:
            return [nums[l][1], nums[r][1]]
        elif s < target:
            l += 1
        else:
            r -= 1
    return [-1, -1] 

