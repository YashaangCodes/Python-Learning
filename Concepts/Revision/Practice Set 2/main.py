print("\nQ1.1 :\n")

num = int(input("Enter a number : "))
if num > 0:
    print(f"{num} is a Positive number!")
elif num == 0:
    print(f"{num} is Zero!")
else:
    print(f"{num} is a Negaative number!")

print("\n")

print("\nQ1.2 :\n")

age = int(input("Enter Your Age : "))
if age >=18:
    print("You are Eligible to vote!")
else:
    print("You are not eligible to vote yet!")

print("\n")

print("\nQ1.3 :\n")

num = int(input("Enter a number : "))
if num%2==0:
    print(f"{num} is an Even Number!")
else:
    print(f"{num} is an Odd Number!")
    
print("\n")

print("\nQ2.1 :\n")

num = int(input("Enter a Day Number (1-7) : "))
match num :
    case 1:
        print(f"Number {num} corresponds to the day Monday!")
    case 2:
        print(f"Number {num} corresponds to the day Tuesday!")
    case 3:
        print(f"Number {num} corresponds to the day Wednesday!")
    case 4:
        print(f"Number {num} corresponds to the day Thursday!")
    case 5:
        print(f"Number {num} corresponds to the day Friday!")
    case 6:
        print(f"Number {num} corresponds to the day Saturday!")
    case 7:
        print(f"Number {num} corresponds to the day Sunday!")
    case _:
        print("Invalid Input!")

print("\n")

print("\nQ2.2 :\n")

print("Simple Calculator".center(25,"-"))
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

print('''
Enter the Number corresponding to the Operation You want to perform : 
[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
'''
)

opp = int(input("Enter : "))

match opp:
    case 1:
        print(f"{num1} + {num2} = {num1+num2}")
    case 2:
        print(f"{num1} - {num2} = {num1-num2}")
    case 3:
        print(f"{num1} X {num2} = {num1*num2}")
    case 4:
        print(f"{num1} / {num2} = {num1/num2}")
    case _:
        print("Invalid Input!")

print("\n")

print("\nQ3.1 :\n")

for i in range(10):
    print(i+1)

print("\n")

print("\nQ3.2 :\n")

num = int(input("Enter a Number : "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

print("\n")

print("\nQ3.3 :\n")

sum = 0
for i in range (1,101):
    sum += i
print(f"The sum of all the numbers from 1 to 100 is {sum}")

print("\n")

print("\nQ3.4 :\n")

