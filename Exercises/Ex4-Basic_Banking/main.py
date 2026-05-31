def Account_Setup():
    global user_name, primay_balance
    user_name = input("Enter the Account holder's Name : ")
    primay_balance = float(input("Enter the Primary Balance : "))
    Action()

def Action():
    para = """
    What Action do you want to perform :
    1] Deposit
    2] Withdraw
    3] Check current Balance
    4] View Transaction History
    """
    print()

