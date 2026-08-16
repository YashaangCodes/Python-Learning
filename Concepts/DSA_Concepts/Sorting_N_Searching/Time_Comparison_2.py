import random
import time
import matplotlib.pyplot as plt

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

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

# Time Comparison
sizes = [100, 500, 1000, 2000]

insertion_time = []
selection_time = []
merge_time = []
quick_time = []

for size in sizes :
    data = random.sample(range(size*10),size)

    # Insertion Sort
    arr = data.copy()
    start = time.perf_counter()
    insertion_sort(arr)
    end = time.perf_counter()

    insertion_time.append(end - start)

    # Selection Sort
    arr = data.copy()
    start = time.perf_counter()
    selection_sort(arr)
    end = time.perf_counter()

    selection_time.append(end - start)

    # Merge Sort
    arr = data.copy()
    start = time.perf_counter()
    merge_sort(arr)
    end = time.perf_counter()

    merge_time.append(end - start)

    # Quick Sort
    arr = data.copy()
    start = time.perf_counter()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.perf_counter()

    quick_time.append(end - start)


