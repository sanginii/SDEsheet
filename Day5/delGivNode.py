#The approach is to copy the next node’s value in the deleted node. Then, link node to next of next node. This does not delete that node but indirectly it removes that node from the linked list.
class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next

        