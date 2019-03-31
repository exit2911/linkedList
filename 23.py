"""

delete the middle node
use a counter and skip to next node when reach the node we want to delete
the middle node is the result of the list size floor divided by 2

"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None
    
    def print_list(self):
        
        node = self.head
        
        while node:
            print(node.data)
            node = node.next
            
            
    def print_skip(self):
        # find the size of the list, then roughly find the middle node by floor dividing the size by 2
        node = self.head
        current = self.head
        count = 0
        size = 0
        while node:
            
            size += 1
            node = node.next            
        mark = size//2
        
        while current:
            
            count += 1
            print(current.data)
            
            if count == mark:
                current = current.next.next
            else:
                current = current.next
                
             
        
        
            
llist = LinkedList()            
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(1)
sixth = Node(1)


llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

llist.print_skip()
