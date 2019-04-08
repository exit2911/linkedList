"""
write code to partition a linked list around a value x such that all nodes 
less than x come before x and all nodes greater than x are on the right

if x is within the linked list, x can be anywhere in the right partition 

tips:
    
    use 2 linked lists, one with values less than x and one with values that are equal to or greater than x
    iterate through the entire linked list

- randomly add one node in front of another. then assemble the list without initialization
"""


"""
write code to partition a linked list around a value x such that all nodes 
less than x come before x and all nodes greater than x are on the right
if x is within the linked list, x can be anywhere in the right partition 
tips:
    
    use 2 linked lists, one with values less than x and one with values that are equal to or greater than x
    iterate through the entire linked list
- randomly add one node in front of another. then assemble the list without initialization
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
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self, new_data): 
        new_node = Node(new_data) #think of class as a bag. set new_node variable to a value
        new_node.next = self.head #new node.next is now a copy of the current head
        self.head = new_node  
    
    def assem(self):
        the_list = self.head
        llist = [1,2,3]
        
        for i in range(3):
            
            new_node = Node(llist[i])
            
            new_node.next = self.head
            self.head = new_node
            
            
        return the_list
        
    def partition(self,partition):
      
        node = self.head
        
        while node:
            
            if node.data < partition:
                left_node = Node(node.data)
                left_node.next = self.head
                self.head = left_node
            else:
                
              while left_node:
                  
                  
                  if left_node.next == None:
                      
                      left_node.next = Node(node.data)
            
                  else:
                      
                      left_node = left_node.next
        node = node.next          
                      
                      
        return left_node
    
        
      
        
if __name__ == "__main__":
    
    
    
        
    llist = LinkedList()
    llist.head = Node(5)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    
    llist.head.next = second
    second.next = third
    third.next = fourth
    llist.partition(3)
    llist.printList()
    
    

