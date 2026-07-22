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