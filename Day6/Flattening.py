class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child
#bruteforce
def flattenLinkedList(head):
        a = []
        i = head
        while i:
            a.append(i.val)  
            j=i.child
            while j:
                a.append(j.val) 
                j=j.child
            i=i.next 
        a.sort()
        new_head = ListNode(a[0])
        curr = new_head
        for i in a[1:]:
            curr.child = ListNode(i)
            curr.next = None
            curr=curr.child
        return (new_head) 

#optimal
class Solution:
    def flattenLinkedList(self, head):
        def merge (a, b):
            dummy = ListNode()
            tail = dummy 
            while a and b:
                if a.val<b.val:
                    tail.child=a
                    a=a.child
                else:
                    tail.child=b
                    b=b.child
                tail=tail.child
            while a:
                tail.child=a
                a=a.child
                tail=tail.child
            while b:
                tail.child=b
                b=b.child 
                tail=tail.child
            return dummy.child
        if not head or not head.next:
            return head 
        head.next = self.flattenLinkedList(head.next) 
        head = merge(head,head.next) 
        head.next = None
        return head
            
            

            