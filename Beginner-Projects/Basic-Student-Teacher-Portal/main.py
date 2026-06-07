import os

def file_path(base_dir, *arg):

    cur_dir = os.getcwd()
    target_dir = os.path.join(cur_dir, base_dir , *arg)

    return target_dir


def view_personal(role,user_name):
    
    user_info_path = file_path("Resources", role, user_name, "info.txt")
    with open(user_info_path,'r') as file :
        info = file.read()
        print(f"\n{info}\n")
    return

def view_role(role):

    role_list_path = file_path("Resources", role ,f"{role}_List.txt")

    with open(role_list_path,'r') as file:
        r_list = file.read()
    
    while True:
        print(f"\n{r_list}\nEnter exit to go back\n")
        user_name = input(f"Enter the name of the {role} to view furthe details : ").title()

        if user_name.lower() == "exit":
            return
        else :
            user_path = file_path("Resources",role ,user_name)

            if os.path.isdir(user_path) :
                role_info_path = file_path("Resources",role ,user_name,"info.txt")
                with open(role_info_path,'r') as file:
                    info = file.read()
                    print(f"\n{info}\n")
            else :
                print("Invalid Input!\n Please Enter the names mentioned in the list")
    

def select_teacher(student_name):

    teach_list_path = file_path("Resources","Teacher","Teacher_List.txt")
    with open(teach_list_path,'r') as file:
        t_list = file.read()
    
    while True:
        print(f"Enter the name of the Teacher you want to be assigned to\nEnter exit to go back\n{t_list}\n")
        teach_name = input("Enter : ").title()

        if teach_name.lower() == "exit":
            return
        else :
            teach_path = file_path("Resources","Teacher" ,teach_name)

            if os.path.isdir(teach_path):

                teach_status_path = file_path("Resources","Teacher",teach_name,"status.txt")
                if os.path.exists(teach_status_path) :
                    print(f"{teach_name} is no longer a part of this Institution\n Select someone else\n")
                    continue

                student_info_path = file_path("Resources","Student",student_name,"info.txt")
                
                with open(student_info_path,'r') as file:
                    text_list = file.readlines()

                if f"{teach_name}\n" in text_list:
                    print("This Teacher is already assigned to you\nSelect someone else\n")
                    continue
                
                teach_info_path = file_path("Resources","Teacher",teach_name,"info.txt")

                with open(teach_info_path,'a') as file:
                    file.write(f"{student_name}\n")

                
                add_index = text_list.index('Assigned Teachers : \n') + 1
                text_list.insert(add_index,f"{teach_name}\n")

                with open(student_info_path,'w') as file:
                    file.writelines(text_list)
                
                print("Continue Selecting Teachers or exit\n")

            else :
                print("Invalid Input!\n Please Enter the names mentioned in the list")
            

def leave(role,user_name):

    role_pass_path = file_path("Resources",role,user_name,"password.txt")

    with open(role_pass_path,'r') as file:
        password = file.read()
    
    while True:
        pass_check = input("Enter your Password to Leave Institution (Enter exit to go back) : ")

        if pass_check == password:
            break
        elif pass_check.lower() == "exit" :
            print("You have been Logged Out.\n Please Log in again\n")
            return
        else :
            print("Invalid Password!")

    role_status_path = file_path("Resources",role,user_name,"status.txt")
    with open(role_status_path,'w') as file:
        file.write("Left Institution")

    role_info_path = file_path("Resources",role,user_name,"info.txt")
    with open(role_info_path,'a') as file:
        file.write("\n----Left Institution----")
        
    setup_window()
    return

def grade_students(teach_name):
    
    teach_info_path = file_path("Resources","Teacher",teach_name,"info.txt")

    with open(teach_info_path,'r') as file:
        info_list = file.readlines()
    
    text = "".join(info_list[4:])

    while True:
        print(f"Enter the name of the Student you want to Grade\nEnter exit to go back\n{text}\n")
        student_name = input("Enter : ").title()

        if student_name.lower() == "exit":
            return
        else :

            student_info_path = file_path("Resources","Student",student_name,"info.txt")

            if not os.path.exists(student_info_path):
                print("Invalid Input!\nEnter the names mentioned\n")
                continue
            
            student_status_path = file_path("Resources","Student",student_name,"status.txt")

            if os.path.exists(student_status_path):
                print("This student has left the institution\nGrading not allowed\n")
                continue

            grd_list = ["O","A","B","C","D","F"]
            while True:

                grade = input("Enter Grade [O,A,B,C,D,F]: ").upper()
                if grade in grd_list:
                    break
                elif grade.lower() == "exit":
                    return
                else:
                    print("Invalid Input! ")
                
            subject = info_list[3]

            with open(student_info_path,'r') as file:
                stud_info_list = file.readlines()
            
            if subject in stud_info_list:
                ch_index = stud_info_list.index(subject) + 1
                stud_info_list[ch_index] = grade
                
                with open(student_info_path,'w') as file:
                    file.writelines(stud_info_list)

            else:
                with open(student_info_path,'a') as file:
                    file.write(f"{subject}{grade}\n")
            print("Student has been Graded!\n")
            
            
def suspend(teach_name):

    teach_info_path = file_path("Resources","Teacher",teach_name,"info.txt")

    with open(teach_info_path,'r') as file:
        info_list = file.readlines()
    
    text = "".join(info_list[4:])

    while True:
        print(f"Enter the name of the Student you want to Suspend\nEnter exit to go back\n{text}\n")
        student_name = input("Enter : ").title()

        if student_name.lower() == "exit":
            return
        else :
            student_info_path = file_path("Resources","Student",student_name,"info.txt")

            if not os.path.exists(student_info_path):
                print("Invalid Input!\nEnter the names mentioned\n")
                continue
            
            student_status_path = file_path("Resources","Student",student_name,"status.txt")

            if os.path.exists(student_status_path):
                print("This student is no longer a part of the college\nSelect someone else\n")
                continue
            
            with open(student_status_path,'w') as file:
                file.write("Suspended!")
            
            with open(student_info_path,'a') as file:
                file.write(f"\n----SUSPENDED by {teach_name}----\n")
            
            print(f"{student_name} has been suspended!\n")


def student_interface(student_name):

    text = """
Enter the number corresponding to the action : 
[1] View Personal Info
[2] View Teachers
[3] Select Teachers
[4] Leave Institution
[5] Log out
"""
    # ac_dic = {"1" : view_personal}


    while True:
        print(text)
        action = input("Enter : ")
        
        if action == "1":
            view_personal("Student",student_name)

        elif action == "2":
            view_role("Teacher")

        elif action == "3":
            select_teacher(student_name)
        
        elif action == "4":
            leave("Student",student_name)
            return

        elif action == "5":
            print("You have logged out")
            setup_window()
            return
        
        else:
            print("Invalid Input\n")

def teacher_interface(teacher_name):
    text = """
Enter the number corresponding to the action : 
[1] View Personal Info
[2] View Students
[3] Grade Your Students
[4] Suspend Students
[5] Leave Institution
[6] Log out
"""
    # ac_dic = {"1" : view_personal}

    while True:
        print(text)
        action = input("Enter : ")
        
        if action == "1":
            view_personal("Teacher",teacher_name)

        elif action == "2":
            view_role("Student")

        elif action == "3":
            grade_students(teacher_name)

        elif action == "4":
            suspend(teacher_name)
        
        elif action == "5":
            leave("Teacher",teacher_name)
            return
        

        elif action == "6":
            print("You have logged out")
            setup_window()
            return
        
        else:
            print("Invalid Input\n")


def user_log(role , role_interface):
        
    while True:
        print("Enter Account's name (Your name)\nType exit to go back\n")
        user_name = input("Enter : ").title()

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
    
    user_status_path = file_path("Resources",role,user_name,"status.txt")
    if os.path.exists(user_status_path):
        print("You are no longer a part of this Institution!")
        setup_window()
        return
    
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

    if role == "Teacher":
        while True:
            teach_code = input("Enter the Teacher's code (Enter exit to go back): ")
            if not teach_code :
                print("Invalid code")
            elif teach_code.lower() == "exit":
                opperation_acc("Create",user_create)
                return
            elif teach_code == "0000":
                break
            else :
                print("Invalid Code")

    while True:
        print(f"Create an Account for {role}\nType exit to go back\n")
        user_name = input("Enter Your Name : ").title()
        
        
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
        text_lines = ["Student Name : \n",f"{user_name}\n","Assigned Teachers : \n", "Grades :\n"]

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
            break
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
