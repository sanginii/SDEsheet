# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        if not curr.next:
            return None
        len=i=0
        while curr:
            len+=1
            curr=curr.next
        if n==len:
            return (head.next)
        curr = head 
        while i < len-n-1:
            curr=curr.next
            i+=1
        curr.next=curr.next.next 
        return head
