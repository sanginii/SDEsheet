from collections import defaultdict
from collections import deque
def verticalTraversal(root):
    mapp = defaultdict(list)
    que = deque([(root,0,0)]) # root,rows,cols
    while que:
        for i in range(len(que)):
            node,row,col = que.popleft()
            mapp[col].append((row,node.val))
            if node.left:
                que.append((node.left,row+1,col-1))
            if node.right:
                que.append((node.right,row+1,col+1))
    result = []
    for col in sorted(mapp.keys()):
        nodes = sorted(mapp[col])
        result.append([val for i,val in nodes])
    return result