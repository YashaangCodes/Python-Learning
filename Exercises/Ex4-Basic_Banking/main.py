import os

def account_setup():
    global prm_balance , cur_dir
    
    user_name = input("Enter Account Holder's Name : ")

    cur_dir = os.getcwd()

    if not os.path.exists(f"{cur_dir}/{user_name}"):
        os.mkdir(f"{cur_dir}/{user_name}")
    else :
        print("Account already exists with this name!")
        return
    
    prm_balance = int(input("Enter the primary Balance : "))



def deposit():
    print("Money will be deposited")

def withdraw():
    print("Money is Withdrawn")

def check_balance():
    
    print(f"Your current Balance is : {prm_balance}")

def view_history():
    print("History will be showed")

def delete_account():
    
    del_name = input("Enter the Account's Name which you want to delete : ")

    if os.path.exists(f"{cur_dir}/{del_name}"):
        os.rmdir(f"{cur_dir}/{del_name}")
    else:
        print("There is no Account with this name present")
        return
    


def interface_window():

    base_dir = os.getcwd()
    target_dir = os.path.join(base_dir, "Exercises", "Ex4-Basic_Banking")
    
    if not os.path.exists(f"{target_dir}/Resources"):
        os.mkdir(f"{target_dir}/Resources")

    os.chdir(f"{target_dir}/Resources")

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
