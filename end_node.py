
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
      
class LinkedList: 
      
        # Function to initialize head 
        def __init__(self): 
            self.head = None
      
        # Function to insert a new node at the beginning 
       
       def push(self, new_data): 
            new_node = Node(new_data) 
            new_node.next = self.head 
            self.head = new_node 
       
       def printList(self): 
            temp = self.head 
            while(temp): 
                print (temp.data)
                temp = temp.next   
       
       def append(self, new_data):
    
            new_node = Node(new_data)
            if self.head is None:
                self.head = new_node
                return
            
            last = self.head
            
            while (last.next):
                last = last.next
                
            last.next = new_node
    
