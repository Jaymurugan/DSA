# Watch the videos. Very confusing but important.
# First we create a Merge function which merges the sorted list.
# then we create a sort function which sorts the merged lists.
def merge(list1, list2): # Takes 2 sorted list and sorts them together into one list.
    combined = [] # We are combine the 2 lists into a new list and we can call this new list as combined.
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

def merge_sort(my_list): # Now we are looking at merge sort in which we sort a single list by breaking it into multiple list and then re mergering them. We will use the merge func we created to merge them back together.
    if len(my_list) == 1: # If we only have a item then it's already sorted hence we dont have to run the future commands to break it in half.
        return my_list
    mid_index = int(len(my_list)/2) # We are finding the mid value. We used the int method because mid could be a decimal value.
    left = merge_sort(my_list[:mid_index]) # The left values from mid. We used merge_sort recursively as we need to divide it multiple times and assign the right and left values for each break down.
    right = merge_sort(my_list[mid_index:]) # The right values from mid.
    return merge(left,right) # Now due to recursion, we know all the list are sorted as they have been broken up to individual pieces.



x = [1,3,5,7,9]
y = merge_sort(x)
print(y)