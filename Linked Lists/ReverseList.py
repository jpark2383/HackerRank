"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    curr = head
    n = None
    p = None
    while curr is not None:
        n = curr.next
        curr.next = p
        p = curr
        curr = n
    head = p
    return head
        
      
  
  
  
  
  
  
  
  
