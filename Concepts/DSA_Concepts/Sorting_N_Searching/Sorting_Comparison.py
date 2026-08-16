import random

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Quick Sort
def quick_sort(arr, start, end):

    if start < end:
        pivot_index = partition(arr, start, end)

        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):

    # First element as pivot
    pivot = arr[start]

    left = start + 1
    right = end

    while True:

        while left <= right and arr[left] <= pivot:
            left += 1

        while left <= right and arr[right] >= pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]

    arr[start], arr[right] = arr[right], arr[start]

    return right

data = random.sample(range(420),20)

insertion_data = insertion_sort(data)
selection_data = selection_sort(data)
merge_data = merge_sort(data)
quick_sort(data, 0, len(data) - 1)

print("The Output of these Sorting are as follows".center(50," "))
print("\nInsertion Sort :", insertion_data)
print("\nSelection Sort :", selection_data)
print("\nMerge Sort :", merge_data)
print("\nQuick Sort :", data)

