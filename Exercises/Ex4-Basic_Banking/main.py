def Account_Setup():
    global user_name, primay_balance
    user_name = input("Enter the Account holder's Name : ")
    primay_balance = float(input("Enter the Primary Balance : "))
    Action_Window()

def Deposit():
    pass

def Withdraw():
    pass

def Check_Balance():
    pass

def View_History():
    pass

def Quit():
    print("Thank You for Trusting Us... Haave a Good Day")
    return 1


def Action_Window():
    para = """
    What Action do you want to perform :
    1] Create Account
    2] Deposit
    3] Withdraw
    4] Check Current Balance
    5] View Transaction History
    6] Quit
    """
    print(para)

    action = input("Either Enter the number or the word (EG - 2 OR Deposit) : ").strip().capitalize()

    action_dict = {"1" : "Create Account", "2" : "Deposit", "3" : "Withdraw", "4" : "Check Current Balance", "5" : "View Transaction History", "6" : "Quit"}

    if action not in action_dict.keys() and action not in action_dict.values():
        print("Invalid Action")
        Action_Window()
    
    if action == "1" or action == "Create Account" :
        Account_Setup()
    elif action == "2" or action == "Deposit" :
        Deposit()
    elif action == "3" or action == "Withdraw" :
        Withdraw()
    elif action == "4" or action == "Check Current Balance" :
        Check_Balance()
    elif action == "5" or action == "View Transaction History" :
        View_History()
    else :
        Quit()
    return 1


Action_Window()
