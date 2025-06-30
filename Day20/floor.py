def find_floor(root, key):
    floor = None
    while root:
        if root.key == key:
            return root
        elif key > root.key:
            floor = root
            root = root.right
        else:
            root = root.left
    return floor