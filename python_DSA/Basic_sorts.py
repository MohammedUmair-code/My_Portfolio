vals = [4, 2, 6, 5, 1, 3]
def bubble_sort(arr):
    for i in range(len(arr)):
        idx = 0
        for _ in range(len(arr) - (1+i)):

            if arr[idx] > arr[idx+1]:
                arr[idx], vals[idx+1] = arr[idx+1], arr[idx]
                
            idx += 1 
    return arr

# sorted_vals = bubble_sort(vals)
# print(sorted_vals)

def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        if arr[i] > arr[min_index]:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            pass
    return arr


# sorted_vals = selection_sort(vals)
# print(sorted_vals)

def insert_sort(my_list):
    for i in range(1, len(my_list)):
       temp = my_list[i]
       j = i-1
       while temp < my_list[j] and j >=0 :
           my_list[j+1] = my_list[j]
           my_list[j] = temp
           j -= 1
    return my_list

arr = [4, 2, 6, 5, 1, 3]
print(insert_sort(arr))





