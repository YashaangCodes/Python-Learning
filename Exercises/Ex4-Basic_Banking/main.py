def Account_Setup():
    print("Acc will be created")

def Deposit():
    print("Money will be deposited")

def Withdraw():
    print("Money is Withdrawn")

def Check_Balance():
    print("Balance will be checked")

def View_History():
    print("History will be showed")

def Interface_Window():
    para = """
        What Action do you want to perform :
        1] Create Account
        2] Deposit
        3] Withdraw
        4] Check Current Balance
        5] View Transaction History
        6] Quit
        """
    ac_dict = { "1" : Account_Setup , "2" : Deposit , "3" : Withdraw , "4" : Check_Balance , "5" : View_History }

    while True:
        
        print(para)
        
        action = input("Enter the Number corresponding to the action (Eg - For Deposit enter 2)) : ")
        
        if action in ac_dict:
            ac_dict[action]()
        elif action == "6":
            print("Thank You for Trusting Us... Have a Good Day")
            break
        else :
            print("Invalid Action")

Interface_Window()
