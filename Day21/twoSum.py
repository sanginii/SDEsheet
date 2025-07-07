class BSTIterator:
    def __init__(self, root, forward=True):
        self.stack = []
        self.forward = forward
        self._push_all(root)

    def _push_all(self, node):
        while node:
            self.stack.append(node)
            node = node.left if self.forward else node.right

    def next(self):
        node = self.stack.pop()
        val = node.val
        if self.forward:
            self._push_all(node.right)
        else:
            self._push_all(node.left)
        return val

    def has_next(self):
        return len(self.stack) > 0

def findTarget(root, k: int) -> bool:
    if not root:
        return False

    left_iter = BSTIterator(root, forward=True)   # inorder
    right_iter = BSTIterator(root, forward=False) # reverse inorder

    left_val = left_iter.next()
    right_val = right_iter.next()

    while left_val < right_val:
        s = left_val + right_val
        if s == k:
            return True
        elif s < k:
            if left_iter.has_next():
                left_val = left_iter.next()
            else:
                return False
        else:
            if right_iter.has_next():
                right_val = right_iter.next()
            else:
                return False

    return False
