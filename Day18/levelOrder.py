from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_key):
        self.root = TreeNode(root_key) 

    def levelOrder(self, root): 
        
        ans = []
        if not root:
            return ans
        que = deque()
        que.append(root) 
        while que:
            level = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                level.append((node.val))
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right) 
            ans.append(level) 
        return ans

bt = BinaryTree(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)

print("Level Order:")
print (bt.levelOrder(bt.root))