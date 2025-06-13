class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None

#recursion 
def inorder(root, a):
    if root:
        inorder(root.left, a)
        a.append(root.val)
        inorder(root.right, a)

#stack
def inorder_iterative(root):
    stack = []
    curr = root
    result = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right

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
inorder(root, a)
print (a) 


