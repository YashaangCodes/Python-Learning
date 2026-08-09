def merge_sort(arr, reverse = False, merge_count = 0, rec_count = 0, rec_level = 0) :

    if len(arr) <= 1:
        return arr, merge_count, rec_count + 1, rec_level + 1

    left_arr = arr[ : len(arr)//2]
    right_arr = arr[len(arr)//2 : ]
    
    left_arr , left_merge_count , left_rec_count , rec_level = merge_sort(left_arr)
    right_arr , right_merge_count , right_rec_count , rec_level = merge_sort(right_arr)

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

    return arr, left_merge_count + right_merge_count + 1, left_rec_count + right_rec_count + 1, rec_level + 1

print("Enter the list with spaces in between (Eg : 4 5 2 9 1):")
items = list(map(int,input().split()))

sorted_items,m_count,r_count,r_level = merge_sort(items)
print("Sorted Numbers :",*sorted_items,f"\nMerge Count : {m_count}\nRecursion Count : {r_count-1}\nRecursion Level : {r_level}\n")

sorted_items_reverse,m_count,r_count,r_level = merge_sort(items,reverse=True)
print("Reverse Sorted Numbers :",*sorted_items_reverse,f"\nMerge Count : {m_count}\nRecursion Count : {r_count-1}\nRecursion Level : {r_level}\n")
