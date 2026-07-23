print("\nQ1.1 :\n")

name = "Yashaang Adhikari"
print(name[0])
print(name[-1])
print(len(name))

print("\nQ1.2 :\n")

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

print("\nQ2.1 :\n")

text = "Python Programming"
print(text[:6])
print(text[-6:])
print(text[1::2])

print("\nQ2.2 :\n")

print(text[::-1])

print("\nQ3.1 :\n")

text = " i love python programming "
text = text.strip()
print(text)
text = text.title()
print(text)
print(text.count("o"))

print("\nQ3.2 :\n")

text = "123abc"
print(text.isalnum())

print("\nQ4.1 :\n")

sent = "My name is {} and I am {} years old"
name = "John"
age = 25
print(sent.format(name,age))

print("\nQ4.2 :\n")

print(f"My name is {name} and I am {age} years old")

print("\nQ5.1 :\n")

sent = "Coding in Python is fun"
sent = sent.replace("fun","awesome")
print(sent)

print("\nQ5.2 :\n")

print(sent.index("Python"))

print("\nQ5.3 :\n")

print(sent.upper())

print("\nQ6.1 :\n")

vowels = ["a","e","i","o","u"]
text = input("Enter your sentence : ").lower()
count = 0
for alp in vowels:
    count += text.count(alp)

print(f"There are {count} vowels in the sentence")

print("\nQ6.2 :\n")

text = input("Enter your string : ")
if text == text[::-1]:
    print("Your string is a palindrome!")
else:
    print("Your string is not a palindrome!")


