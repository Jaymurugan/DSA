# In Queues it's first in first out.
class Node:
    def __init__(self, value, next= None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def enqueue(self,value): # Enqueue in just getting in line. Adding a value in queue.
        new_node = Node(value)
        if self.first is None: #if the queue is none. We could also do if length == 0.
            self.first = new_node
            self.last = new_node 
        else:
            self.last.next = new_node # changing the last pointer from None to new_node
            self.last = new_node # Now changing the last to new_node.
        self.length += 1

    def dequeue(self): # Removing the first element as it's first come first serve.
        if self.length == 0:
            return None
        temp = self.first # we create a temp before the if as we need to return the temp value. It's pointing to the first element. We could have put it inside the else statement if we doesnt have to return it.
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next # moving the first pointer to the 2nd pointer
            temp.next = None #temp was assigned as the first pointer. We are removing it by assinging none to it's next value.
        self.length -= 1
        return temp.value

#leetcodes for queues and stacks: 20,  
