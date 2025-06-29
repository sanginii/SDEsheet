class Solution:
    def flatten(self, root) -> None:
        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                # Connect it to curr's right subtree
                prev.right = curr.right
                # Move left subtree to right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
