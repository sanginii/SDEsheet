from typing import Optional
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
def create_linked_list(arr):
    dummy = Node()
    tail = dummy
    for val in arr:
        tail.next = Node(val)
        tail = tail.next
    return dummy.next
class Node: 
    def __init__ (self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def merge (self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        dummy = Node()
        tail = dummy 
        while a and b:
            if a.val<b.val:
                tail.next=a
                a=a.next
            else:
                tail.next=b
                b=b.next
            tail=tail.next
        while a:
            tail.next=a
            a=a.next
            tail=tail.next
        while b:
            tail.next=b
            b=b.next 
            tail=tail.next
        return dummy.next

    
a = create_linked_list([1, 3, 5])
b = create_linked_list([2, 4, 6])

s = Solution()
merged = s.merge(a, b)
print_list(merged) 