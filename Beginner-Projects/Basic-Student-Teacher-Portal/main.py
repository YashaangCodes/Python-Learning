import os

def file_path(base_dir, *arg):

    cur_dir = os.getcwd()
    target_dir = os.path.join(cur_dir, base_dir , *arg)

    return target_dir

def sign_in():
    print("You will be signed in")

def create():
    print("Account will be created")


def setup_window():

    check_dir = os.path.join(os.getcwd(), "Beginner-Projects", "Basic-Student-Teacher-Portal")
        
    if os.path.isdir(check_dir):
        os.chdir(check_dir)
    
    resource_path = file_path("Resources")

    if not os.path.isdir(resource_path):
        os.mkdir(resource_path)

    teacher_path = file_path("Resources","Teacher")
    student_path = file_path("Resources","Student")

    if not os.path.isdir(teacher_path):
        os.mkdir(teacher_path)
    if not os.path.isdir(student_path) :
        os.mkdir(student_path)

    sign_up_window()


def sign_up_window():

    text = """
[1] Log in to an Existing Account
[2] Create a New Account
[3] Quit"""
    print(text)

    ac_dic = {"1" : sign_in , "2" : create}

    while True:
        action = input("Enter the corresponding Number : ")

        if action in ac_dic:
            ac_dic[action]()
        elif action == "3":
            print("You have quited")
            break
        else:
            print("Invalid Input")


if __name__=="__main__":
    setup_window()



