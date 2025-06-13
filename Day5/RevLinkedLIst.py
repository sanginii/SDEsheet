#bruteforce with stack
# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self,data):
#         self.stack.append(data)
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return -1
#     def is_empty(self):
#         return len(self.stack)==0
    
# def rev (self):
#         current = self.head
#         s = Stack()
#         while current:
#             s.push(current.data) 
#             current=current.next 
#         current = self.head
#         while current:
#             current.data = s.pop()
#             current=current.next
    

#optimal with recursion 
class Node:
    def __init__ (self, data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__ (self):
        self.head = None
    def append (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current=current.next
        current.next=new_node
    def prepend (self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete (self,key):
        current = self.head
        if current and current.data==key:
            self.head = current.next
            return
        prev = None
        while current and current.data!=key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
    def rev (self, head):
        if head is None or head.next is None:
            return head 
        new_head = self.rev(head.next) 
        head.next.next = head
        head.next = None
        return new_head

    def print_list (self):
        current = self.head
        while current:
            print (current.data, end="->")
            current = current.next
        print("None") 

l1 = Linkedlist()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
l1.append(50)
l1.print_list()
l1.head = l1.rev(l1.head)
l1.print_list()


#optimal
# def rev (self):
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next=prev
#             prev=current
#             current=next_node
#         self.head = prev 