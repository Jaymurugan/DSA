def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0 ,-1): # We interate it len-1 times and until it reaches 0th by decrementing len-1 by 1 and so on.
        for j in range(i): # This for loop is the loop that's going to move forward thru the list. For example: if my_list is "Gay" then i would be 2 first and then it will decrease by 1 to become 1 and so on as i is range(len(my_list),0,-1)
            if my_list[j] > my_list[j+1]: # if it's bigger we swap. Since j is in range(i), it'll go thru all the scenarios.
                temp = my_list[j]
                my_list[j]  = my_list[j+1]
                my_list[j+1] = temp
    return my_list

print(bubble_sort([2,4,5,2,4,2,5,2,1]))
