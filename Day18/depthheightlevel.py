def height(node):
    if node is None:
        return -1  # height in terms of edges
    return 1 + max(height(node.left), height(node.right))

def depth_of_node(root, key, depth=0):
    if root is None:
        return -1
    if root.key == key:
        return depth
    left = depth_of_node(root.left, key, depth + 1)
    if left != -1:
        return left
    return depth_of_node(root.right, key, depth + 1)

def level_of_node(root, key):
    depth = depth_of_node(root, key)
    return depth + 1 if depth != -1 else -1 