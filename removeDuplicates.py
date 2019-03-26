
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
    
    def removeDuplicates(self): #remove duplicates for an sorted list
        temp = self.head 
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.data == temp.next.data: 
                new = temp.next.next
                temp.next = None
                temp.next = new 
            else: 
                temp = temp.next
        return self.head 
    

    
      
        
if __name__ == "__main__":
    
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(3)
    
    llist.head.next = second
    second.next = third
    third.next = fourth
    llist.removeDuplicates()
    llist.printList()
    
    
