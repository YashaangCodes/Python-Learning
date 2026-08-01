import time
import random

# Linear Search

def linear(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Binary Search

def binary(data,target):
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target :
            return mid
        elif data[mid] > target :
            high = mid - 1
        else :
            low = mid + 1
    return -1

sizes = [100, 500, 1000, 5000, 10000]
linear_time = []
binary_time = []

for size in sizes:

    items = sorted(random.sample(range(size*10),size))
    mark = items[-1]

    start = time.time()
    linear(items,mark)
    linear_time.append(time.time() - start)

    start = time.time()
    binary(items,mark)
    binary_time.append(time.time() - start)


