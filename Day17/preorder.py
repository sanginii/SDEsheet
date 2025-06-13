class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None

#recursion
def preorder(root, a):
    if root:
        a.append(root.val)
        preorder(root.left, a)
        preorder(root.right, a)

#stack
def preorder_iterative(root):
    if not root:
        return []
    
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7) 
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11) 
root.right.left.right = Node(13)
root.right.right.left = Node(14) 
a = []
preorder(root, a)
print (a) 


