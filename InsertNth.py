"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    res = Node(data, None)
    if not head:
        return res
    elif position == 0:
        res.next = head
        head = res
        return head
    else:    
        fast = head
        slow = head
        for x in range(position - 1):
            slow = slow.next
        fast = slow.next
        slow.next = res
        res.next = fast
        return head
  
  
  
  
  
  
  
  
  
