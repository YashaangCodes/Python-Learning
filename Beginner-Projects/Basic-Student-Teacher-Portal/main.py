import os

def file_path(base_dir, *arg):

    cur_dir = os.getcwd()
    target_dir = os.path.join(cur_dir, base_dir , *arg)

    return target_dir


def student_interface(student_name):
    print(f"Student {student_name} Interface")

def teacher_interface(teacher_name):
    print(f"The Teacher {teacher_name} can use Features and they will be done here")


def user_log(role , role_interface):
        
    while True:
        print("Enter Account's name (Your name)\nType exit to go back\n")
        user_name = input("Enter : ")

        if not user_name:
            print("Invalid Input")
        elif user_name.lower() == "exit":
            opperation_acc("Log into",user_log)
            return
        else:
            user_path = file_path("Resources", role ,user_name)

            if not os.path.isdir(user_path):
                print("No Account with such name exists!")
                continue
            else:
                break
    
    pass_info_path = file_path("Resources", role ,user_name,"password.txt")

    with open(pass_info_path,'r') as file:
        read_pass = file.read()
    
    while True:
        print("Enter exit to go to the Log In window")
        pass_check = input("Enter the Password : ")

        if read_pass == pass_check:
            break
        elif pass_check.lower() == "exit":
            opperation_acc("Log into",user_log)
            return
        else:
            print("Invalid Password!\n")

    print(f"You are now Logged In as {user_name}\n")
    
    role_interface(user_name)



def user_create(role , role_interface):
        
    while True:
        print(f"Create an Account for {role}\nType exit to go back\n")
        user_name = input("Enter Your Name : ")
        
        
        if not user_name:
            print("Invalid Input")
        elif user_name.lower() == "exit":
            opperation_acc("Create",user_create)
            return
        else:
            user_path = file_path("Resources", role ,user_name)

            if not os.path.isdir(user_path):
                os.mkdir(user_path)
                add_name_path = file_path("Resources", role ,f"{role}_List.txt")

                with open(add_name_path,'a') as file:
                    file.write(f"[ ] {user_name}\n")
                break
            else:
                print("Account alredy Exists!")
    

    while True:
        user_pass = input("Enter a password for this Account : ")
        
        if not user_pass :
            print("Invalid Password")
        elif len(user_pass) < 5 :
            print("Password too short!")
        else:
            break
            
    if role == "Teacher":
        teach_sub = input("Enter the Subject You Teach : ")
        text_lines = ["Teacher Name : \n",f"{user_name}\n", "Subject : \n",f"{teach_sub}\n","Assigned Students : \n"]

    else:
        text_lines = ["Student Name : \n",f"{user_name}\n","Assigned Teachers : \n", "None\n", "Grades :\n"]

    info_path = file_path(user_path,"info.txt")
    password_path = file_path(user_path,"password.txt")

    with open(info_path,'w') as file:
        file.writelines(text_lines)
    
    with open(password_path,'w') as file:
        file.write(user_pass)


    print(f"You are now Logged in as {user_name}")

    role_interface(user_name)

def opperation_acc(operation, user_operation):
    
    start = f"{operation} an Account as a Teacher or a Student?\n"
    text = """
Enter [1] for Teacher
Enter [2] for Student
Enter [3] to Exit to the main Window\n 
"""
    ac_dic = {"1" : ["Teacher",teacher_interface] , "2" : ["Student",student_interface]}

    while True:
        print(start,text)
        action = input("Enter : ")
        
        if action in ac_dic:
            role_list = ac_dic[action]
            user_operation(role_list[0],role_list[1])
            break
        elif action == "3":
            setup_window()
            break
        else:
            print("Invalid Input\n")



def setup_window():

    text = """
[1] Log in to an Existing Account
[2] Create a New Account
[3] Quit"""
    print(text)

    while True:
        action = input("Enter the corresponding Number : ")

        if action == "1":
            opperation_acc("Log into",user_log)
            break
        elif action == "2":
            opperation_acc("Create",user_create)
        elif action == "3":
            print("You have quited")
            break
        else:
            print("Invalid Input\n")

def main():

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

    teach_list = file_path("Resources","Teacher","Teacher_List.txt")
    stud_list = file_path("Resources","Student","Student_List.txt")

    if not os.path.exists(teach_list):
        with open(teach_list,'w') as file:
            file.write("Teachers List : \n")

    if not os.path.exists(stud_list):
        with open(stud_list,'w') as file:
            file.write("Students List : \n")

    setup_window()



if __name__=="__main__":
    main()
