# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def rev (head: Optional[ListNode])-> Optional[ListNode]:
            if head is None or head.next is None:
                return head 
            new_head = rev(head.next) 
            head.next.next = head
            head.next = None
            return new_head
        def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
            slow=head
            fast=head
            while fast and fast.next and fast.next.next:
                slow=slow.next
                fast=fast.next.next 
            return slow
        if not head or not head.next:
            return True
        midNode = middleNode(head)
        revList = rev(midNode.next) 
        curr1=head
        curr2=revList
        is_palindrome = True
        while curr2:
            if curr1.val != curr2.val:
                is_palindrome = False
                break
            curr1 = curr1.next
            curr2 = curr2.next

        midNode.next = rev(revList)  
        return is_palindrome

            
