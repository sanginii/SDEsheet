class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
#bruteforce using O(N) extra space for map 
#time - O(2N) 2 times traversal
#space O(N)for mapping + O(N)for cloning
def copyRandomList(head):
    mpp = {}
    temp = head
    while temp:
        mpp[temp] = Node(temp.val) 
        temp=temp.next
    temp = head
    mpp[None]=None
    while temp:
        mpp[temp].next = mpp[temp.next]
        mpp[temp].random = mpp[temp.random] 
        temp=temp.next
    return mpp[head] 

#optimal
#time O(N)+O(N)
#space O(N) for clone
def copyRandomList(head):
        if not head:
            return None
        
        # Step 1: Clone each node and insert it right after the original node
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        
        # Step 2: Assign random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Step 3: Separate the original and copied lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
        
        return copy_head