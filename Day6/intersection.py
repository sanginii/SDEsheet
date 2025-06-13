class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head
# utility function to check presence of intersection
#bruteforce
def intersectionPresent(head1, head2):
    while head2 != None:
        temp = head1
        while temp != None:
            # if both nodes are same
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next
    # intersection is not present between the lists
    return None
#better
# def intersectionPresent(head1, head2):
#     st = set()
#     while head1 != None:
#         st.add(head1)
#         head1 = head1.next
#     while head2 != None:
#         if head2 in st:
#             return head2
#         head2 = head2.next
#     return None


# utility function to print linked list created
def printList(head):
    while head.next != None:
        print(head.val, end='->')
        head = head.next
    print(head.val)
if __name__ == '__main__':
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 3)
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 4)
    head1 = head
    head = head.next.next.next
    headSec = None
    headSec = insertNode(headSec, 3)
    head2 = headSec
    headSec.next = head
    print('List1: ', end='')
    printList(head1)
    print('List2: ', end='')
    printList(head2)
    answerNode = intersectionPresent(head1, head2)
    if answerNode == None:
        print('No intersection')
    else:
        print('The intersection point is', answerNode.val)

# Output:

# List1: 1->3->1->2->4
# List2: 3->2->4
# The intersection point is 2

# Time Complexity: O(m*n)

# Reason: For each node in list 2 entire list 1 is iterated. 

# Space Complexity: O(1)

# Reason: No extra space is used.