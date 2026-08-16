# Linear Search

def linear(data,target):
    print(f"Original Data : {data}")
    for i in range(len(data)):
        if data[i] == target:
            print(f"Target {target} found at index {i}")
            return True
    return False

# Binary Search

def binary(data,target):
    data.sort()
    print(f"Sorted Data : {data}")
    low = 0
    high = len(data)-1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target :
            print(f"Target {target} found at index {mid}")
            return True
        elif data[mid] > target :
            high = mid - 1
        else :
            low = mid + 1
    return False

items = [2, 5, 7, 8, 9, 0, 6, 41, 23]
mark = 0

print("\nLinear Search : ")
if not linear(items,mark):
    print("\nTarget wasn't Found!")

print("\nBinary Search : ")
if not binary(items,mark):
    print("\nTarget wasn't Found!")

