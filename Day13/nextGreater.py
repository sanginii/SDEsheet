nums1 = [4,1,2]
nums2 = [1,3,4,2]
stack = []
next_greater = {} 
# Traverse nums2 from right to left
for num in reversed(nums2):
    # Maintain a decreasing stack
    while stack and stack[-1] <= num:
        stack.pop()
    # If stack is empty, no greater element
    next_greater[num] = stack[-1] if stack else -1
    stack.append(num)

# Build the result using the map
print ([next_greater[num] for num in nums1]) 