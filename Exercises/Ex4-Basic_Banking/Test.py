# dic = {"1" : "Create Account", "2" : "Deposit", "3" : "Withdraw", "4" : "Check Current Balance", "5" : "View Transaction History", "6" : "Quit"}
# print(dic.keys())
# print(dic.values())

# action = input("Enter : ").strip().capitalize()
# if action not in dic.keys() and action not in dic.values():
#     print("No")
# else :
#     print("Yes" , action)

# text = input("Enter: ").strip().capitalize()

# # print(text)
# text= input("Enter : ").lower()
# print(text)

def create():
    print("Acc will be created")
    return

def deposit():
    print("Money will be deposited")
    return

def withdraw():
    print("Money is Withdrawn")
    return

# ac_dic = {1 : create() , 2 : deposit() , 3 : withdraw()}
# ac_dic[2]

while True :
    ac_dic = {1 : create , 2 : deposit , 3 : withdraw}
    action = int(input("Enter the action : "))

    if action in ac_dic.keys():
        ac_dic[action]()
    elif action == 4:
        break


    # if action not in [1,2,3]:
    #     print("Invalid Action")
    #     continue
    # for i in range(1,4):
    #     if i == action:
    #         ac_dic[i]()
