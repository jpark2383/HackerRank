"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head == None:
        return Node(data,None,None)
    temp = head
    while temp != None:
        if temp.data >= data:
            ins = Node(data, temp, temp.prev)
            temp.prev = ins
            if ins.prev is None:
                return temp
            else:
                ins.prev.next = ins
                return head
        if temp.next is None:
            ins = Node(data, None, temp)
            temp.next = ins
            break
        temp = temp.next
    return head
  
  
  
  
  
  
  
