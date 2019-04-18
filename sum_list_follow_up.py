

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 22:23:43 2019

@author: vyho
"""

#import the append function or create a new class

#count the difference in digits

#how about just add digits to the front?
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
            flist_size = 0
            slist_size = 0        
            count = 0
          
                
                
            while fList is not None or sList is not None:
                
                if fList:
                    flist_size += 1
                    fList = fList.next
                    
                if sList:
                    slist_size += 1
                    sList = sList.next
              
                if  flist_size - slist_size is not None:
                    
                    if flist_size > slist_size:
                        zero_count = flist_size - slist_size
                        while sList:
                            while count < zero_count:
                                sList.head = 0
                                sList.head.next = sList.head
                                count += 1
                    
                    else:      
                        
                        zero_count =  slist_size - flist_size
                        while fList:
                            while count < zero_count:
                                fList.head = 0
                                fList.head.next = fList.head
                                count += 1
                                
                                
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
