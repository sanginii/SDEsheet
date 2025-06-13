class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None
def rightSideView(root):
    def  view(root, level, dt):
        if root:
            if level not in dt:
                dt[level] = root.val
            view(root.right, level+1, dt)
            view(root.left, level+1, dt)
    dt = {}
    view(root, 0, dt) 
    return list(dt.values())

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6) 
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11) 
root.right.left.right = Node(13)
print (rightSideView(root)) 