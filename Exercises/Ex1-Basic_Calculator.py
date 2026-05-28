a = input("Enter the first number : ")
b = input("Enter the Second number : ")
o = input("Enter the Operation: ")

if o == "+": # Basic Calculator
	print(a, "+", b, "=", float(a) + float(b))
elif o == "-":
	print(a, "-", b, "=", float(a) - float(b))
elif o == "*":
	print(a, "*", b, "=", float(a) * float(b))
elif o == "/":
	print(a, "/", b, "=", float(a) / float(b))
elif o == "//":
	print(a, "//", b, "=", float(a) // float(b))
elif o == "%":
	print(a, "%", b, "=", float(a) % float(b))
else :	
	print("Invalid Operation")
 