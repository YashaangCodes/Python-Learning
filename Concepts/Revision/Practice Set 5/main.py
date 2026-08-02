print("\nQ1.1 :\n")

fruits = ["apple","banana","cherry"]
print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))

print("\nQ1.2 :\n")

numbers = [(i+1) for i in range(10)]
for num in numbers[:3]:
    print(num,end=" ")
print()
for num in numbers[-3:]:
    print(num,end=" ")
print()
print("\nQ2.1 :\n")

numbers = [5,2,9,1,7]
numbers.sort()
numbers.append(10)
numbers.remove(2)
print(numbers)

print("\nQ2.2 :\n")

names = ["Alice","Bob","Charlie"]
names.insert(1,"David")
print(names)

print("\nQ3 :\n")

coordinates = (10,20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50 # Will throw an Error
coordinates = list(coordinates)
coordinates[0] = 50
coordinates = tuple(coordinates)
print(coordinates)

