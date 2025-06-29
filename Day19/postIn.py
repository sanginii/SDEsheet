class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    idx_map = {val: i for i, val in enumerate(inorder)}
    
    def helper(in_left, in_right, post_left, post_right):
        if in_left > in_right or post_left > post_right:
            return None

        # Root is the last node in postorder range
        root_val = postorder[post_right]
        root = TreeNode(root_val)

        # Index of root in inorder array
        idx = idx_map[root_val]
        left_tree_size = idx - in_left

        # Build left and right subtrees
        root.left = helper(in_left, idx - 1, post_left, post_left + left_tree_size - 1)
        root.right = helper(idx + 1, in_right, post_left + left_tree_size, post_right - 1)

        return root

    return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
