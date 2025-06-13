from collections import deque

def bottomView(root):
    if not root:
        return []

    mapp = dict()  # col -> node.val
    que = deque([(root, 0)])  # (node, column)

    while que:
        node, col = que.popleft()
        mapp[col] = node.val  # overwrite with the latest (bottommost)

        if node.left:
            que.append((node.left, col - 1))
        if node.right:
            que.append((node.right, col + 1))

    # Sort by column (left to right)
    result = [mapp[col] for col in sorted(mapp.keys())]
    return result
