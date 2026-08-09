def merge_sort(arr, reverse = False):

    if len(arr) <= 1:
        return arr

    left_arr = arr[ : len(arr)//2]
    right_arr = arr[len(arr)//2 : ]
    
    merge_sort(left_arr)
    merge_sort(right_arr)

    i = 0
    j = 0

    if reverse == True:
        k = 1
    else :
        k = 0
   
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            if reverse == True :
                arr[-k] = left_arr[i]
            else :
                arr[k] = left_arr[i]
            i += 1
        else :
            if reverse == True :
                arr[-k] = right_arr[j]
            else :
                arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        if reverse == True :
            arr[-k] = left_arr[i]
        else :
            arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        if reverse == True :
            arr[-k] = right_arr[j]
        else :
            arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr

items = [57, 23, 89, 12, 45, 67, 1]
sorted_items = merge_sort(items)
print(sorted_items)
sorted_items_reverse = merge_sort(items,True)
print(sorted_items_reverse)

