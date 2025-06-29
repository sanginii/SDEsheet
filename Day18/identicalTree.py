def isSameTree(p, q):
    # Both nodes are None → trees match here
    if not p and not q:
        return True

    # One is None and the other isn't → mismatch
    if not p or not q:
        return False

    # Node values differ → mismatch
    if p.key != q.key:
        return False

    # Recurse on left and right children
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
