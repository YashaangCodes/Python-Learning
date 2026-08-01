# Linear Search

def linear(data,target):
    for i in range(len(data)):
        if data[i] == target:
            print(f"Target {target} found at index {i}")

items = [2, 5, 7, 8, 9, 0, 6, 41, 23]
mark = 0

linear(items,mark)
