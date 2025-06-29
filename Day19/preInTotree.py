from typing import List, Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    # Map value -> index in inorder for O(1) lookups
    inorder_index = {val: i for i, val in enumerate(inorder)}
    
    def helper(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
        if pre_left > pre_right or in_left > in_right:
            return None

        # Root is always the first element in preorder range
        root_val = preorder[pre_left]
        root = TreeNode(root_val)

        # Find root in inorder
        idx = inorder_index[root_val]
        left_tree_size = idx - in_left

        root.left = helper(pre_left + 1, pre_left + left_tree_size, in_left, idx - 1)
        root.right = helper(pre_left + left_tree_size + 1, pre_right, idx + 1, in_right)

        return root

    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
