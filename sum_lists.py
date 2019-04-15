"""
add sum list

2 linked lists of 2 reversed numbers. each node has one digit. write an algorithm to add

adding 2 numbers require starting at the last digits. hence, we don't have to reverse the 2 linked lists. we only need to reverse the result linked list

modulo works for all nodes. no need to distinguish the location of the carrying digit

Created on Sun Apr 14 16:08:31 2019

@author: vyho
@location: Filicori Zecchini

check the lengths. if one of the 2 has a none node while the other is not, then the other's node is 0
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
                    prev.next = temp
            
                prev = temp                
                if fList:
                    fList = fList.next
                    
                if sList:
                    sList = sList.next
            

first = LinkedList() 
second = LinkedList() 
  
# Create first list 
first.push(5) 
first.push(6) 
first.push(9) 
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
  
