                            
from queue import Queue
from typing import Optional


# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # If the root is null,
        # the width is zero
        if not root:
            return 0

        # Initialize a variable 'ans'
        # to store the maximum width
        ans = 0

        # Create a queue to perform level-order
        # traversal, where each element is a tuple
        # of TreeNode and its position in the level
        q = Queue()
        # Push the root node and its
        # position (0) into the queue
        q.put((root, 0))

        # Perform level-order traversal
        while not q.empty():
            # Get the number of
            # nodes at the current level
            size = q.qsize()
            # Get the position of the front
            # node in the current level
            mmin = q.queue[0][1]

            # Store the first and last positions
            # of nodes in the current level
            first, last = None, None

            # Process each node
            # in the current level
            for i in range(size):
                # Calculate current position relative
                # to the minimum position in the level
                node, cur_id = q.get()
                cur_id -= mmin 

                # If this is the first node in the level,
                # update the 'first' variable
                if i == 0:
                    first = cur_id

                # If this is the last node in the level,
                # update the 'last' variable
                if i == size - 1:
                    last = cur_id

                # Enqueue the left child of the
                # current node with its position
                if node.left:
                    q.put((node.left, cur_id * 2 + 1))

                # Enqueue the right child of the
                # current node with its position
                if node.right:
                    q.put((node.right, cur_id * 2 + 2))

            # Update the maximum width by calculating
            # the difference between the first and last
            # positions, and adding 1
            ans = max(ans, last - first + 1)

        # Return the maximum
        # width of the binary tree
        return ans


def main():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    maxWidth = sol.widthOfBinaryTree(root)

    print(f"Maximum width of the binary tree is: {maxWidth}")


if __name__ == "__main__":
    main()
                           
                        