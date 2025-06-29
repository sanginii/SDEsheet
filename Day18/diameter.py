class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def diameter_of_tree(root):
    diameter = [0]  # Use list to store mutable max value

    def height(node):
        if not node:
            return 0
        lh = height(node.left)
        rh = height(node.right)
        diameter[0] = max(diameter[0], lh + rh)  # update diameter
        return 1 + max(lh, rh)

    height(root)
    return diameter[0]
