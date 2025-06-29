def convertToChildrenSumTree(root):
    if not root:
        return

    def postorder(node):
        if not node or (not node.left and not node.right):
            return

        postorder(node.left)
        postorder(node.right)

        left_val = node.left.val if node.left else 0
        right_val = node.right.val if node.right else 0
        child_sum = left_val + right_val

        # If node value is less than children sum, update node
        if node.val < child_sum:
            node.val = child_sum
        # If node value is greater, propagate down to children
        elif node.val > child_sum:
            diff = node.val - child_sum
            increment(node, diff)

    def increment(node, diff):
        if node.left:
            node.left.val += diff
            increment(node.left, diff)
        elif node.right:
            node.right.val += diff
            increment(node.right, diff)

    postorder(root)
