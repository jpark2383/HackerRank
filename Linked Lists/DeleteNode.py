"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if not head:
        return None
    elif position == 0:
        temp = head.next
        head.next = None
        head = temp
        return head
    else:
        temp = head
        dNode = head
        for x in range (position - 1):
            temp = temp.next
        dNode = temp.next
        temp.next = dNode.next
        dNode.next = None
        return head
  
  
