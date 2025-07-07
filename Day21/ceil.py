def find_ceil(root, key):
    ceil = None
    while root:
        if root.key == key:
            return root
        elif key < root.key:
            ceil = root
            root = root.left
        else:
            root = root.right
    return ceil 