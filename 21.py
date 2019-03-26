"""
2.1

remove duplicates from an unsorted linked list
FOLLOW UP: what if temporary buffer is not allowed

"""



class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None
    
    def printList(self): #traverse a linked list
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next
    
    def removeDuplicates(self):  # remove duplicate method for sorted list
        temp = self.head 
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.data == temp.next.data: 
                temp.next = None #set to none so we can skip this node
                temp.next = temp.next.next 
            else: 
                temp = temp.next
        
     
    
    def removeDup(self):    # remove duplicate method for unsorted list
        
        elements = []
        
        temp = self.head #current node; starting at the head
        
        if temp.next is None:
            return
        while temp.next:
            if temp.data in elements:
               temp.next = None 
               temp.next = temp.next.next
            else:
                
                elements.append(temp.data)
        
                temp = temp.next

        return self
      
        
if __name__ == "__main__":
    
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(1)
    
    llist.head.next = second
    second.next = third
    third.next = fourth
    
    llist.removeDup()
    llist.printList()
    
    
