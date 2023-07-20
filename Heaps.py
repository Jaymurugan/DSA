# Heap is very similar to a Binary Search Tree and it is a form of binary tree. It's different BST as the numbers in heaps are distributed in the same way. We store heaps differently from BST as well.
# Heaps can also have duplicates. # Max he is when we have the highest value at the top. Min heap is when we have the min value at the top.
# We will be storing heaps as list and we won't be creating a Node class. We can either store the first value of the heap in the 0th index of the list or the 1st index of the list. Both are common. We will start off by putting it in the 1st index as the math is a lot easier.

# Now we are going to build a class for the helper methods. Here the first value in the 0th index.
class MaxHeap:
    def __init__(self): # Basic function to create a list and we can call the list heap.
        self.heap = []

    def _left_child(self, index): # Func to get the left child of a particular Node.
        return 2 * index + 1 # the index of the left child of a parent will be twice the index of parent + 1.
    
    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2 # The index of the parent will be the index of the child - 1 divided by 2. The // rounds it to the lower number. For ex: 4.5 will become 4.
    
    def _swap(self, index1, index2): # We pass in 2 indexes and it swaps the nodes in that indexes.
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # We are done with the helper methods. Now let's build the heap.

    def insert(self, value): # Instead of inserting the node in the right place, we insert the node in the nearest postition and compare it with it's parents and swap it until it reaches the right position.
        self.heap.append(value) # We are adding the value we created to the list heap. It's going to get added as the final value.
        current = len(self.heap) - 1 # We are creating a variable called current which is going to point at the index we added the node in. Current is just holding the value of the index.

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]: # We run it until the current value reaches the 0th index or we stop when the parent becomes greater than the child.
            self._swap(current, self._parent(current)) #We are swapping current and it's parent until current becomes smaller than the parent or current becomes the 1st node.
            current = self._parent(current) # Since we swapped parent and the current, We now need the current to point or hold the index value of the parent as value we added is in the parent's place after swapping.


    def remove(self): # When we remove a value from a heap, there is only one value we ever remove and it's the one at the top. Doesn't matter if it's min or max heap.
# After removing the first element there is only one way to make the heap complete and that is to move the right node (last Node) to the first and then we swap all the elements according to it's value. In adding we added down and then sorted it to the top to it's appr spot. Here we are adding the right most element to the top and the sorting it down to it's appr spot.
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop() # Here we pop it node and return the node we popped.
        max_value = self.heap[0] # We know that the first node before removing is the biggest term of all nodes.
        self.heap[0] = self.heap.pop() # We are replacing the 0th index with the last index as we know that when we pop the last index is removed.
        self._sink_down(0) # Since now the last index is in the 0th index we need to move it to it's appropriate location. Hence, we use the _sink_down helper function on the 0th index.
        return max_value # Is going to return the value we popped.
    
    def _sink_down(self, index): # We don't have to pass in an index as we use it to sink the 0th index down in this case but it's useful to write it with the index as we can use it in other scenarios as well.
        max_index = index # We just create a variable called max variable and set it equal to index which holds the index of the 0th element.
        while True:
            left_index = self._left_child(index) # We are getting the left child of the indes we want to sink down.
            right_index = self._right_child(index)
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[index]: # If the left child is greater than the value we try to sink down then we swap. For heap to be complete it doesn't need to have the left or the right index in the end parent. Hence we use this if condition.
                max_index = left_index # We we change the max_index to left index to check if it's bigger or lesser than the right child.
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]: # Here max_index can be either the left index or the index of the value we are trying to sink down. 
                max_index = right_index
            if max_index != index: # Meaning if the max index is either the left or right child, we swap the index with max index.
                self._swap(index, max_index)
                index = max_index
            else:
                return

    


x = MaxHeap()
x.insert(95)
x.insert(75)
x.insert(80)
x.insert(55)
x.insert(60)
x.insert(50)
x.insert(65)

print(x.heap)

x.remove()

print(x.heap)

x.remove()

print(x.heap)

