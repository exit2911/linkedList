
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None
        
    def printList(self): #traverse a linked list
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self, new_data): 
        new_node = Node(new_data) #think of class as a bag
        new_node.next = self.head 
        self.head = new_node 
        
        
      
        
if __name__ == "__main__":
    
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    
    llist.head.next = second
    second.next = third
    third.next = fourth
    
    llist.push(5)
    llist.printList()
    
