def account_setup():
    print("Acc will be created")

def deposit():
    print("Money will be deposited")

def withdraw():
    print("Money is Withdrawn")

def check_balance():
    print("Balance will be checked")

def view_history():
    print("History will be showed")

def delete_account():
    print("Account will be deleted")

def interface_window():
    para = """
        What Action do you want to perform :
        1] Create Account
        2] Deposit
        3] Withdraw
        4] Check Current Balance
        5] View Transaction History
        6] Delete Account
        7] Quit
        """
    ac_dict = { "1" : account_setup , "2" : deposit , "3" : withdraw , "4" : check_balance , "5" : view_history , "6" : delete_account}

    while True:
        
        print(para)
        
        action = input("Enter the Number corresponding to the action (Eg - For Deposit enter 2)) : ")
        
        if action in ac_dict:
            ac_dict[action]()
        elif action == "7":
            print("Thank You for Trusting Us... Have a Good Day")
            break
        else :
            print("Invalid Action")

interface_window()
