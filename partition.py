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
        
        
      
        
if __name__ == "__main__":
    
    the_list = LinkedList()
    the_list.assem()
    
   
    the_list.printList()
    

