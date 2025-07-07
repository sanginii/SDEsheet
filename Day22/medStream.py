class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1  # number of nodes in subtree including self

class OrderStatisticBST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Insert val into the BST, updating size fields. No balancing.
        """
        def _insert(node, val):
            if not node:
                return Node(val)
            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            # update size after insertion
            node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
            return node

        self.root = _insert(self.root, val)

    def kth_smallest(self, k):
        """
        Return the k-th smallest value in the BST (1-based).

        Logic:
        - Let L = size of left subtree.
        - If k == L + 1, current node is the k-th smallest.
        - If k <= L, the k-th smallest is in the left subtree.
        - If k > L + 1, the k-th smallest is in the right subtree.
          Why? Because you've already counted L nodes in the left subtree
          and the current node (1 more). So you've skipped L + 1 nodes so far,
          and want the (k - L - 1)-th smallest node in the right subtree.
        """
        def _kth(node, k):
            if not node:
                raise IndexError("k is out of bounds")

            # number of nodes strictly in left subtree
            left_size = node.left.size if node.left else 0

            # Case 1: current node is the k-th smallest
            if k == left_size + 1:
                return node.val
            # Case 2: k-th smallest is in left subtree
            elif k <= left_size:
                return _kth(node.left, k)
            # Case 3: k-th smallest is in right subtree
            else:
                # We skip left_size nodes in left subtree and the current node,
                # so the relative k in the right subtree is:
                #    k' = k - (left_size + 1)
                new_k = k - (left_size + 1)
                return _kth(node.right, new_k)

        return _kth(self.root, k)

class RunningMedian:
    def __init__(self):
        self.tree = OrderStatisticBST()
        self.count = 0

    def add_num(self, val):
        """Insert a number into the data structure."""
        self.tree.insert(val)
        self.count += 1

    def get_median(self):
        """Return the current median."""
        if self.count == 0:
            return None
        if self.count % 2 == 1:
            # odd count
            return self.tree.kth_smallest((self.count + 1) // 2)
        else:
            # even count
            a = self.tree.kth_smallest(self.count // 2)
            b = self.tree.kth_smallest(self.count // 2 + 1)
            return (a + b) / 2
