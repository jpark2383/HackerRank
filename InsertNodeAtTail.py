"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""
#Python 3

def Insert(head, data):
    temp = head
    if not head:
        return Node(data, None)
    else:
        while temp.next:
            temp = temp.next
        temp.next = Node(data, None)
        return head


  
  
  
  
  
  
