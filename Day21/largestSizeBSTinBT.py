class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
    def largestBSTSubtree(self, root):
        self.max_size = 0
        def postorder(node):
            if not node:
                #is_bst, size, min, max
                return (True, 0, float('inf'), float('-inf'))
            left_is_bst, left_size, left_min, left_max = postorder(node.left)
            right_is_bst, right_size, right_min, right_max = postorder(node.right)
            if left_is_bst and right_is_bst and left_max<node.val<right_min:
                size = left_size+right_size+1
                self.max_size=max(self.max_size, size) 
                return (True, size, min(node.val, left_min), max(node.val, right_max))
            else:
                return (False, max(left_size, right_size), 0, 0)
        postorder(root)
        return self.max_size 