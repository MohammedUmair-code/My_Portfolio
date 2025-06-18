def pivot_helper(my_list):
    idx = 0
    pivot_index = idx
    swap_index = idx

    for i in range(1, len(my_list)):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            my_list[swap_index], my_list[i] = my_list[i],my_list[swap_index]
    my_list[pivot_index], my_list[swap_index] = my_list[swap_index], my_list[pivot_index]
    return swap_index

a = [4, 6, 1, 7, 3, 2, 5]


def quick_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    middle_index =  pivot_helper(my_list)
    my_list1 = my_list[:middle_index]
    my_list2 = my_list[middle_index +1 :]

    quick_sort(my_list1)
    quick_sort(my_list2)

    return my_list


print(quick_sort(a))
