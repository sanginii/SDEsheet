nums = [3, 1, 3, 4, 2]
slow = nums[0]
fast = nums[0]

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
        break

# Step 2: Find entrance to cycle
slow = nums[0]
while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

print (slow) 