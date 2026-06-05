import os

def file_path(base_dir, *arg):

    cur_dir = os.getcwd()
    target_dir = os.path.join(cur_dir, base_dir , *arg)

    return target_dir

def teacher_interface(teacher_name):
    print(f"The Teacher {teacher_name} can use Features and they will be done here")


def teacher_create():
        
    while True:
        print("Create an Account for Teacher\nType exit to go back\n")
        teach_name = input("Enter Your Name : ").strip()
        
        
        if not teach_name:
            print("Invalid Input")
        elif teach_name.lower() == "exit":
            create_acc()
            return
        else:
            teach_path = file_path("Resources","Teacher",teach_name)

            if not os.path.isdir(teach_path):
                os.mkdir(teach_path)
                add_name_path = file_path("Resources","Teacher","Teacher_List.txt")

                with open(add_name_path,'a') as file:
                    file.write(f"[ ] {teach_name}\n")
                break
            else:
                print("Account alredy Exists!")
    
    teach_sub = input("Enter the Subject You Teach : ")

    text_lines = ["Teacher Name : \n",f"{teach_name}\n","Subject : \n",f"{teach_sub}\n","Assigned Students : \n"]
    
    info_path = file_path(teach_path,"info.txt")

    with open(info_path,'w') as file:
        file.writelines(text_lines)
    
    # with open(info_path,'r') as file:  # Experiment
    #     text_read = file.readlines()
    #     print(text_read)

    # if text_read[1] == teach_name:    # Experiment
    #     print("Will Work!")
    # elif text_read[1] == f"{teach_name}\n":
    #     print("Adding a new line will make it work!")
    # else:
    #     print("Won't work!")

    print(f"You are now Logged in as {teach_name}")

    teacher_interface(teach_name)

def student_create():
    print("Student Create acc")


def log_in():
    print("You will be logged in")

def create_acc():
    text = """
Create an Account as a Teacher or a Student?
Enter [1] for Teacher
Enter [2] for Student
Enter [3] to Exit to the main Window\n 
"""
    ac_dic = {"1" : teacher_create , "2" : student_create , "3" : setup_window}

    while True:
        print(text)
        action = input("Enter : ")
        
        if action in ac_dic:
            ac_dic[action]()
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


def setup_window():

    text = """
[1] Log in to an Existing Account
[2] Create a New Account
[3] Quit"""
    print(text)

    ac_dic = {"1" : log_in , "2" : create_acc}

    while True:
        action = input("Enter the corresponding Number : ")

        if action in ac_dic:
            ac_dic[action]()
            break
        elif action == "3":
            print("You have quited")
            break
        else:
            print("Invalid Input\n")


if __name__=="__main__":
    main()



