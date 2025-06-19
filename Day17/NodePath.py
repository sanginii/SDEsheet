# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def allRootToLeaf(self, root):
        def helper(node, path, res):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:
                res.append(list(path))  # make a copy of the current path
            else:
                helper(node.left, path, res)
                helper(node.right, path, res)
            path.pop()  # backtrack

        res = []
        helper(root, [], res)
        return res

