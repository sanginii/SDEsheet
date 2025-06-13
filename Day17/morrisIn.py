#Left->Node
class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None

def inorderTraversal(root):
    a = []
    curr = root
    while curr:
        if not curr.left:
            a.append(curr.val)
            curr = curr.right
        else:
            prev=curr.left
            while prev.right and prev.right != curr:
                prev=prev.right 
            if prev.right == curr:
                prev.right = None
                a.append(curr.val) 
                curr = curr.right 
            else:                                           
                prev.right = curr
                curr = curr.left
    return (a)

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
print (inorderTraversal(root))
