dic = {"1" : "Create Account", "2" : "Deposit", "3" : "Withdraw", "4" : "Check Current Balance", "5" : "View Transaction History", "6" : "Quit"}
print(dic.keys())
print(dic.values())

action = input("Enter : ").strip().capitalize()
if action not in dic.keys() and action not in dic.values():
    print("No")
else :
    print("Yes" , action)

# text = input("Enter: ").strip().capitalize()

# print(text)

