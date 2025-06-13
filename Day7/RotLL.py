# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #brtuteforce space O(1) time O(K*N)
    # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head  
    #     for i in range(k):
    #         curr = head
    #         while curr.next.next:
    #             curr=curr.next
    #         curr.next.next=head
    #         head = curr.next
    #         curr.next=None
    #     return head 

    #optimal O(L)+O(L-K)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head  
        temp = head
        l=1
        while temp.next:
            temp=temp.next
            l+=1
        temp.next = head
        k=k%l
        temp = head
        for i in range (l-k-1):
            temp=temp.next
        head = temp.next 
        temp.next = None
        return head