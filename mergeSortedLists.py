from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists)==0: return
        listHeap=[]
        root=ListNode(0)
        curNode=root
        for Node in lists:
            if Node:
                heappush(listHeap,(Node.val,Node))
        while listHeap:
            pop=heappop(listHeap)
            curNode.next=ListNode(pop[0])
            curNode=curNode.next
            if pop[1].next:
                heappush(listHeap,(pop[1].next.val,pop[1].next))
        return root.next
