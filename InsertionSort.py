# We start from the 2nd item in the list, if it's less than the first item, we swap. then we go to the 3rd item and compare it with the 2nd and so on. If the 5th element is the smallest, we compare it to all the elemnts before it until we reach the first slot and we insert it right there.
def insertion_sort(my_list):
    for i in range(1, len(my_list)): # We start from 1 as explained before we start from the 2nd element.
        temp = my_list[i] # We create a variable to hold the value i. 
        j = i-1 # Since we compare to the item before it, we set j to i-1.
        while temp < my_list[j] and j > -1: # We have a edge case where j might become -1 if we swap any element to the first element. Hence, we say j > -1.
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j-=1 # Since we keep comparing it to the elements before it until it's not smaller anymore.
    return my_list

print(insertion_sort([2,4,5,2,4,2,5,2,1,100,920,910]))

