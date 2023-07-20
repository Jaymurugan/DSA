class Node: #we are creating a class to create a Node.
  def __init__(self,value,next=None):
    self.value = value
    self.next = next

class LinkedList: #We are creating a class to create a linkedlist using the created Node.
  def __init__(self,value): #To create a linkedlist and add the node to it.
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  
  def print_list(self): #Just a function to print the list.
    temp = self.head
    while temp is not None:
      print(temp.value) 
      temp = temp.next

  def append(self,value): #Function to append a node to the existing LL at the end.
    new_node = Node(value)
    if self.head is None: # Could also be written as: if self.length == 0.
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True

  def pop(self): # Function to pop the "final" node. # watch the videos.
    if self.length == 0:
      return None
    temp = self.head #We are creating 2 variable temp and pre to replace head and tail.
    pre = self.head #We created it so that we can assign them to head or tail at the end.
    while(temp.next): #While temp.next is true meaning temp.next is not None or empty.
      pre = temp
      temp = temp.next #here temp will be in the last node which needs to be popped.
    self.tail = pre #pre will be in the node that's previous to the pooped node.
    self.tail.next = None # we are breaking the last Node (temp) and popping it.
    self.length -= 1
    if self.length == 0: #this is after the self.length -= 1 as at the end both head and tail will point at node we need to pop.
      self.head = None
      self.tail = None
    return temp #returning the location of the node we removed. add temp.value to return the value of node instead.

  def prepend(self,value): #Function to add node to the first element. Code is pretty similar to append.
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else: 
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  
  def pop_first(self):
    if self.head is None:
      return None
    temp = self.head #We are creating a temp and assigning it to the head.
    self.head = self.head.next #We are moving the head to the next value.
    temp.next = None #Now we are popping the temp by assing none to it's next value.
    self.length -= 1
    if self.length == 0: #this is after the self.length -= 1 as at the end the tail will point at node we need to pop.
      self.tail = None
    return temp #returning the value of the node we removed. add temp.value to return the value instead of location.
  
  def get(self,index): #We are gonna pass in an index as LL doesnt have index unlike lists and we are gonna return the value at index.
    if index < 0 or index >= self.length: # We are checking if the index is valid.
      return None
    temp = self.head
    for _ in range(index): #we could have said for i in range but it can only be used inside the for loop.
      temp = temp.next
    return temp # Since we returned temp outside the loop we used _ instead of a variable like i. Use temp.value to get value.
  
  def set_value(self,index,value): # Function to change the value in an index. 
    temp = self.get(index) # we are creating a temp and assigning with the get(index) to point at the appropriate node.
    if temp: # For all valid temp values we are changes it's current value to the value we want.
      temp.value = value
      return True
    return False # We are returning false if temp is None or Not valid.
  
  def insert(self,index,value): # Function to insert a value in an given index.
    if index<0 or index>self.length:
      return False
    if index == 0: # If it's the first element, we just prepend.
      return self.prepend(value)
    if index == self.length: # If it's the last element, we just append.
      return self.append(value)
    new_node = Node(value) 
    temp = self.get(index-1) # We create a temp value and set it to the index before the one we want to insert in. 
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
  
  def remove(self,index):
    if index < 0 or index > self.length:
      return None # We returned None here but False in the insert function because here if we are successful we are going to return a node. Not True or False.
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    prev = self.get(index - 1) # We can assign both prev and temp with self.get but it's more efficienct to do it this way according to Big - O.
    temp = prev.next
    prev.next = temp.next # Setting the node previous to the node we want to pop to the next node.
    temp.next = None # Popping the node we need to remove.
    self.length -= 1
    return temp
  
  def reverse(self):
    prev, curr = None, self.head
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next # Variable after temp
    before = None # Variable before temp. We sent it to None as temp begins in the first node.
    for _ in range(self.length):
      after = temp.next
      temp.next = before # This is the code that reverses the LL.
      before = temp
      temp = after

class DoublyLinkedList: # We are creating a new class to build a double LL. Almost everything is similar except it has a prev value with points backwords.
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value) 
      temp = temp.next
  
  def append(self,value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return True
  
  def pop(self):
    if self.length == 0:
      return None
    temp = self.tail # We are creating a temp value to point at the tail value.
    if self.length == 1: # In prev Pop we did this at the end after length -=1 but this is more cleaner and gives the same output.
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev # We are moving the tail value to the prev value.
      self.tail.next = None # breaks the connection between last and the prev value
      temp.prev = None # breaks the last element off.
    self.length -= 1
    return temp
  
  def prepend(self,value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
    self.length += 1
    return True
      
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
      temp.next = None
    self.length -= 1
    return temp.value
  
  def get(self, index): # We can do the same thing we did in single LL but we can optimize it by doing binary search as we have prev.
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    if index < self.length/2:
      for _ in range(index): #if its less then we move from front.
        temp = temp.next
    else: 
      temp = self.tail
      for _ in range(self.length - 1, index, -1): # Important. We are starting the loop from the tail and going backwards. # method to get for loop backwards.
        temp = temp.prev
    return temp
  
  def set_value(self, index, value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False

  def insert(self, index, value):
    if index < 0 or index > self.length: #it's not index - 1 as we will add the new value to index making it add one to index.
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node = Node(value)
    before = self.get(index-1) #creating a self pointer and assining it to the prev index of what we need to join it in.
    after = before.next #next of before. Has the same index of the index we need to join.
    new_node.prev = before
    new_node.next = after
    before.next = new_node
    after.prev = new_node
    self.length += 1
    return True
  
  def remove(self, index):
    if index < 0 or index > self.length:
      return None
    temp = self.head
    if index == 0:
      return self.pop_first()
    if index == self.length - 1:
      return self.pop()
    else:
      temp = self.get(index)
      before = temp.prev
      after = temp.next
      before.next = after
      after.prev = before
      temp.prev = None
      temp.next = None
    self.length -= 1
    return temp.value

      

    

my_l = DoublyLinkedList(0)
my_l.append(1)
my_l.append(3)
my_l.append(1)
my_l.remove(2)
my_l.print_list()







  


# Leetcodes to study for this: 206, 876, 141, 1285, 19, 86, 83, 21, 




    
  
    


  
