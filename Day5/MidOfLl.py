#Optional[ListNode] means The parameter head can either be a ListNode or None.
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next 
        return (slow)

sol = Solution()
node3= ListNode(3)
node2=ListNode(2,node3)
node1=ListNode(1,node2)
head = ListNode(0,node1)
print (sol.middleNode(head).val) 

