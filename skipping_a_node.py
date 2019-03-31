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
        
        node = self.head
        count = 0
        final = 2
        while node:
            
            count += 1
            print(node.data)
            
            if count == final:
                node = node.next.next
            else:
                node = node.next
                
             
        
        
            
llist = LinkedList()            
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(1)



llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

llist.print_skip()
