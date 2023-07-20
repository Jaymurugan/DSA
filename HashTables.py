# When constructing a hastable we should always have a prime number of addresses. It's because using a prime number increases the amount of randomness which reduces chances of collision.
class HashTable:
    def __init__(self, size= 7): # If we don't dont set a parameter to something, it just becomes the default which is 7.
        self.data_map = [None] * size # We will call this list data map. Hence here we are creating a list with 7 items in it and all of the contains None.

    def __hash(self,key): # Now we are creating a hash method. Hash is where we pass to key to to determine the address where we store the key value pair.
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map) # the ord(letter) gets the ascii of each letter as we are looping thru it. We are multipling it by 23 as it's a prime no. We can plug any prime no in there. Now we are getting the remainder by dividing it by the len. If we divide it by 7 then the remainder is going to be from 0 to 6 which are our keys.
        return my_hash # It's going to be from 0 to 6.
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,": ", val)
    
    def set_item(self, key, value): # We are setting the key and the value into a slot in the map.
        index = self.__hash(key) # We get which index the key is going to.
        if self.data_map[index] == None: # We only want to create an empty list if its not already been created.
            self.data_map[index] = [] # Now we are placing an empty list in that index. Remember the the key and values are stores in a list inside a list in the map. For example in the index of 4 in the map there could be 2 lists such as [['cold' : 1400 ], ['hot' : 2800]]
        self.data_map[index].append([key,value]) # Now we are adding the key and the value in that index. 

    def get_item(self, key): # We get getting the value using the key.
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):# We are looping thru the list inside the index as there could be collision resulting in multiple lists of keys and values present in the list in the index.
                if self.data_map[index][i][0] == key: # So in the index there can be multiple lists, hence we look for the 0th element in every list(i) as the 0th element is the key. if the key of the first element is not a match we go to the next one until we find the key.
                    return self.data_map[index][i][1] # as the 1st element in the found list is the value.
        return None # If the key is not present in the hash table.

    def keys(self): # Now we are creating a keys function where we go thru the keys in the hash table and return all the keys in that list.
        all_keys = [] # We are creating a empty list to put all the keys into.
        for i in range(len(self.data_map)): # We are moving along the data map.
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])): # Now we are going thru the lists inside each element of the datamap.
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    

my = HashTable()

my.set_item('bolts', '1400')
my.set_item('washers', '50')
my.set_item('lumber', '70')

print(my.keys())


# Both Insert and Lookup by Key in Hashtables have a Big O of O(1). But that doesnt mean its always better than Binary Search Tree in Insert and Lookup. Binary Search Trees are sorted which makes them better at searching for all values that fall within a range.
# The Big O of O(1) is for looking up the key not the value. 

#Leetcodes to solve: 442, 387, 49, 1, 128

