"""
add sum list

2 linked lists of 2 reversed numbers. each node has one digit. write an algorithm to add

modulo works for all nodes. no need to distinguish the location of the carrying digit

Created on Sun Apr 14 16:08:31 2019

@author: vyho
@location: Filicori Zecchini

"""

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
               
        def addTwoLists(self,fList,sList):
            
            temp = None
            prev = None
           
            carry = 0
            
            while fList is not None or sList is not None:
                fdata = 0 if fList is None else fList.data 
                sdata = 0 if sList is None else sList.data 
                        
                
                sum = carry + fdata + sdata
                
                if sum < 10:
                    
                    carry = 0
                 
                else:
                
                    carry = 1
                    
                    sum = sum % 10 
                    
                temp = Node(sum)
            
                if self.head == None:
                    self.head = temp
                else:
                    temp.next = self.head 
                    self.head = temp 
               # prev = temp                
                if fList:
                    fList = fList.next
                    
                if sList:
                    sList = sList.next
            

first = LinkedList() 
second = LinkedList() 
  
# Create first list 
first.push(9) 
first.push(1) 
first.push(1) 
print ("First List is ") 
first.printList() 

# Create second list 
second.push(2) 
second.push(2) 
print ("\nSecond List is ")
second.printList() 
  
# Add the two lists and see result 
res = LinkedList() 
res.addTwoLists(first.head, second.head) 
print ("\nResultant list is ")
res.printList() 
