class Solution:
    def kthSmallest(self, root, k: int) -> int:
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.right
            curr = stack.pop()
            k-=1
            if k==0:
                return curr.val
            curr = curr.left 