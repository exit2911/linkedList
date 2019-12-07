"""

doubly linked list

add to front

remove

print as string

"""


class Node: #attributes and methods
    
    def __init__(self,data):
        
        self.data = data # data of the current node
        self.next = None # node links to next node
        self.previous = None # node links to previous node
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def add(self,data):
        
        node = Node(data)
        
        if self.head == None: #if there is no current head. head is the data in node
            self.head = node
        else:
            node.next = self.head # if there is a head. next node = head and current node is the input data
            node.next.prev = node
            self.head = node # the input data is now the head
            
    def search(self,k):
        
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data ==k):
                    return p
                p = p.next
                
            if p.data == k: # an extra if statement here because the while loop ends without going over the end node
                return p
        return None
    
    def remove(self, data):
        p = self.head
        if p != None: # if the list is not empty
            
            if p.data == data: #case the removal is head
                p = p.next
                p.next = p.next.next
                
            while p.next != None:              
                if p.data == data:
                    
                    p.prev.next = p.next
                    p.next.prev = p.prev
                p = p.next
                
            if p.data == data: #case the removal is tail
                p.prev.next = None
        
                
        
    def __str__(self): # method to iterate through the link list and add all elements to a string for printing
        
        s = ""
        p = self.head
        if p != None: #action if the list is not empty
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s
                
                
            
l = LinkedList()
 
 
l.add( 'a' )
l.add( 'b' )
l.add( 'c' )

print(l)

l.remove('b')

print(l)
