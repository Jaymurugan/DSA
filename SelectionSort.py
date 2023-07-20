# Pretty similar to bubble sort but instead of sorting with the value we sort thru the index and instead of the last value being sort first, here the first value is sorted first.
def selection_sort(my_list):
    for i in range(len(my_list) - 1): # We are going thru the list.
        min_index = i # Since we sort the first value first, the min index is going to be 0 and then after the forst sort it's going to be 1 and so on.
        for j in range(i + 1, len(my_list)): # i+1 is going to be our start value and len(my_list) is going to be our end value. We start with i+1 as we already set i as min.
            if my_list[j] < my_list[min_index]:
                min_index = j # If j is less that min we set j as min. Note here min is i.
        if i !=  min_index: # We i in not min in index then we know j is the min index hence we swap i and j.
            temp = my_list[i] # We are swapping min_index and i as j is less than i.
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

print(selection_sort([2,4,5,2,4,2,5,2,1]))


