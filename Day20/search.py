def searchBST(self, root, val: int):
    while root:
        if root.val == val:
            break
        elif root.val > val:
            root=root.left
        else:
            root=root.right
    return root