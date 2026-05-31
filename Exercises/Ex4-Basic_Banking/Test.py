dic = {1 : "One", 2 : "Two", 3 : "Three"}
print(dic.keys())
print(dic.values())

action = input("Enter : ")
if action in dic.keys() or dic.values():
    print("Yes" , action)

    


