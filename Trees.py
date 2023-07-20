# Insert is faster in linked list as it's O(1) while binary tree is o(logn)
# While lookup and remove is faster in Binary tree as it's O(logn) while linked list is o(n)

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None # We can add value to the init func and write self.value = value and self.root = value. But instead of creating a node and setting it to the root we set the root to node so that we can insert it in the insert function.
    
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True  # We return True as if the the root is None then we don't want to carry the lines that follows.
        temp = self.root # We set a pointer called temp to the root.
        while(True):  # True is always going to be true. The way we are going to break out of the while loop is by hitting a return statement at somepoint in the loop.
            if new_node.value == temp.value:
                return False # as we can't insert a number that already exists in the Binary Tree
            if new_node.value < temp.value:
                if temp.left is None:  
                    temp.left = new_node
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
my = BinarySearchTree()
my.insert(47)
my.insert(21)
my.insert(76)
my.insert(18)
my.insert(27)
my.insert(52)
my.insert(82)

print(my.contains(21))
print(my.contains(22))

# Leetcode questions: 226, 
            
            







