queue = []
max = 5

def isempty():
    if not queue:
        return True
    else:
        return False

def isFull():
    if len(queue) == max:
        return True
    else:
        return False

def enqueue(item):
    if isFull():
        print("Queue Overflow")
    else:
        queue.append(item)

def dequeue():
    if isempty():
        print("Queue Empty")
    else:
        return queue.pop(0)

data = [1,2,3,4]

for i in data:
    enqueue(i)

print(queue)

print(isempty())
print(isFull())