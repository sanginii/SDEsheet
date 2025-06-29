def maxPathSum(self, root) -> int:
    def findSum(root, mx):
        if not root:
            return 0 
        ls = max(0, findSum(root.left, mx))
        rs = max(0, findSum(root.right, mx))
        mx[0] = max(mx[0], ls+rs+root.val)
        return root.val+max(ls,rs)
    mx = [float("-inf")]
    findSum(root, mx) 
    return mx[0]