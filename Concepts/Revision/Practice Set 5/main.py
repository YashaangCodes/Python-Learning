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

print("\nQ4.1 :\n")

my_set = {1,2,3,3,4}
print(my_set)

print("\nQ4.2 :\n")

my_set.add(5)
my_set.discard(2)
print(my_set)
if 4 in my_set:
    print(True)
else:
    print(False)

print("\nQ4.3 :\n")

a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("\nQ5.1 :\n")

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
student["grade"] = "A+"
student["city"] = "Delhi"
print(student)

print("\nQ5.2 :\n")

info = {"Yashaang" : 8686868686, "John" : 9898989898, "Doe" : 4747474747}
print(info.keys())
print(info.values())
for name,num in info.items():
    print(f"{name} : {num}")

    