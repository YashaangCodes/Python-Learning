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

print("\nQ4.1 :\n")

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5))

print("\nQ4.2 :\n")

def sum_of_digits(n):
    if n < 10 :
        return n
    return (n%10) + sum_of_digits(n//10)

print(sum_of_digits(1234))

print("\nQ5.1 :\n")

import math
print(math.sqrt(144))

print(math.sin(math.radians(90)))

print("\nQ5.2 :\n")

import requests as rq
data = rq.get("https://api.github.com")
print(data.json())

print("\nQ6.1 :\n")

def increment():
    counter = 0
    print(counter)
    counter += 1
    print(counter)
increment()
increment()

print("\nQ6.2 :\n")

def multiply(a,b):
    '''
    Returns the multiplied value of a and b
    
    Parameters : 
    a : integer
    b : integer

    Returns : An Interger value of multiplication of a and b
    '''
    return a * b
print(multiply(4,7))
help(multiply)

print("\nQB.1 :\n")

def fibo(count, num1=0,num2=1):
    if count == 0 :
        return ""
    return f"{num1} " + fibo(count-1,num2,num1+num2)

print(fibo(10))

print("\nQB.2 :\n")

def safe_divide(a,b):
    if b == 0:
        return "Cannot divide by Zero!"
    return a/b
print(safe_divide(10,2))
print(safe_divide(10,0))

print("\nQB.3 :\n")

import my_utils as mu
print(mu.is_even(10))
print(mu.is_even(11))