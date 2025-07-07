# Definition for a binary-tree node / doubly-list node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left   # will serve as 'prev' in DLL
        self.right = right  # will serve as 'next' in DLL

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        Converts a binary tree into a doubly-linked list in-place,
        following the in-order sequence. Returns the head of the list.
        """
        if not root:
            return None

        self.prev = None
        self.head = None

        def inorder(cur):
            if not cur:
                return
            # left
            inorder(cur.left)

            # visit / rewire
            if self.prev:
                # link the previous node <-> current
                self.prev.right = cur
                cur.left = self.prev
            else:
                # this is the very first (smallest) node → head of list
                self.head = cur

            # mark current as previous before going right
            self.prev = cur

            # right
            inorder(cur.right)

        inorder(root)
        return self.head
