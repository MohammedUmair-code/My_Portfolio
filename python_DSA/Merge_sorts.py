def merge_helper(my_list1, my_list2):
    sorted_list = []
    i, j = 0, 0
    while i < len(my_list1) and j < len(my_list2):
        if my_list1[i] < my_list2[j]:
            sorted_list.append(my_list1[i])
            i += 1 
        if my_list1[i] > my_list2[j]:
            sorted_list.append(my_list2[j])
            j += 1
    sorted_list.extend(my_list1[i:])
    sorted_list.extend(my_list2[j:])  #Work through this
    return sorted_list

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    new1 = []
    new2 = []
    stop = len(my_list)/ 2 

    for i in my_list:
        if my_list.index(i) < stop:
            new1.append(i)
        if my_list.index(i) >= stop:
            new2.append(i)
    merge_sort(new1)
    merge_sort(new2)

    return merge_helper(new1, new2)

a = [5, 4, 7, 1, 3, 2, 8, 6]
print(merge_sort(a))