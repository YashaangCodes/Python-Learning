import os

def get_balance(info_path):
    with open(info_path, "r") as file:
        line = file.readline()
    
    return int(line.split("=")[1])
    

def save_balance(info_path,base_balance):
    with open(info_path, "w") as file :
        file.write(f"Balance={base_balance}")


def account_setup():

    user_name = input("Enter Account Holder's Name : ")

    if not os.path.exists(f"{cur_dir}/{user_name}"):
        os.mkdir(f"{cur_dir}/{user_name}")
    else :
        print("Account already exists with this name!")
        return
    
    prm_balance = int(input("Enter the primary Balance : "))

    filepath = os.path.join(cur_dir, user_name, "info.txt")
    file_balance = os.path.join(cur_dir, user_name, "balance.txt")
    
    with open(filepath, "w") as file :
        file.write(f"Account Holder's Name : {user_name}\nPrimary Balance : {prm_balance}\n\nTransaction History :- \n")

    save_balance(file_balance,prm_balance)

    

def deposit():
    
    user_name = input("Enter Account Holder's Name into which you want to deposit: ")
    dp_money = int(input("Enter the amount you want to Deposit : "))

    filepath = os.path.join(cur_dir, user_name, "info.txt")
    file_balance = os.path.join(cur_dir, user_name, "balance.txt")

    balance = get_balance(file_balance) + dp_money

    save_balance(file_balance, balance)

    with open(filepath, "a") as file:
        file.write(f"Deposited : +{dp_money}\n")


def withdraw():
    user_name = input("Enter Account Holder's Name from which you want to withdraw: ")
    wd_money = int(input("Enter the amount you want to Withdraw : "))

    filepath = os.path.join(cur_dir, user_name, "info.txt")
    file_balance = os.path.join(cur_dir, user_name, "balance.txt")

    balance = get_balance(file_balance) - wd_money

    save_balance(file_balance, balance)

    with open(filepath, "a") as file:
        file.write(f"Withdrawn : -{wd_money}\n")

def check_balance():
    
    user_name = input("Enter Account Holder's Name whose balance you want to check: ")
    file_balance = os.path.join(cur_dir, user_name, "balance.txt")
    balance = get_balance(file_balance)
    
    print(f"Your Current Balance is : {balance}")


def view_history():

    user_name = input("Enter Account Holder's Name whose transaction history you want to check: ")
    
    filepath = os.path.join(cur_dir, user_name, "info.txt")

    with open(filepath,"r") as file:
        info = file.read()
    print(f"\n{info}")

def delete_account():
    
    del_name = input("Enter the Account's Name which you want to delete : ")

    if os.path.exists(f"{cur_dir}/{del_name}"):
        filepath = os.path.join(cur_dir, del_name, "info.txt")
        file_balance = os.path.join(cur_dir, del_name, "balance.txt")

        os.remove(filepath)
        os.remove(file_balance)
        os.rmdir(f"{cur_dir}/{del_name}")
    else:
        print("There is no Account with this name present")
        return
    


def interface_window():
    global cur_dir

    base_dir = os.getcwd()
    target_dir = os.path.join(base_dir, "Exercises", "Ex4-Basic_Banking")
    
    if not os.path.exists(f"{target_dir}/Resources"):
        os.mkdir(f"{target_dir}/Resources")

    os.chdir(f"{target_dir}/Resources")
    cur_dir = os.getcwd()

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
