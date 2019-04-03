"""
print kth to last element in a linked list

"""
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:

    def __init__(self):
        self.head = None
    
   
      
    def displayK(self,k): #print kth to last element in the linked list
        
      
        self.k = k
        size = 0
        
        temp = self.head
        while temp.next:
            size += 1
            temp = temp.next
        
        target_count = size + 1 - k
        count = 0
       
        current = self.head
        while current.next:
           count += 1
          
           if count == target_count:
               break
           else:    
                current = current.next
        return print("kth to last is",current.data)
         
        
        
    
        
        
      

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



llist.displayK(1)
