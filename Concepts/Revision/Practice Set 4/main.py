print("\nQ1.1 :\n")

def greet():
    print("Hello, Pyhton Learner!")

greet()

print("\nQ1.2 :\n")

def square(num):
    return num**2

print(square(2))
print(square(6))
print(square(9))

print("\nQ2.1 :\n")

def full_name(first,last):
    return first + " " + last

print(full_name("Yashaang","Adhikari"))

print("\nQ2.2 :\n")

def calculate_area(length, width = 10):
    return length * width

print(calculate_area(10,5))
print(calculate_area(10))

print("\nQ3.1 :\n")

add = lambda x,y : x + y
print(add(5,6))

print("\nQ3.2 :\n")

num_list = [1, 2, 3, 4, 5]
square_list = list(map(lambda x : x**2,num_list))
print(*square_list)
