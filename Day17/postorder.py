#Left → Right → Root 
class Node:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None
#recursive
def postorder(root, a):
    if root:
        postorder(root.left, a)
        postorder(root.right, a)
        a.append(root.val)

#stack
def postorder_iterative_single_stack(root):
    result = []
    stack = []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            # if right child exists and traversing node from left child, move to right child
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.val)
                last_visited = stack.pop()

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
postorder(root, a)
print (a) 


