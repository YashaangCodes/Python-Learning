import os

base_dir = os.getcwd()

target_dir = os.path.join(base_dir,"Concepts","Os_Module")

if os.getcwd() != target_dir:
    os.chdir(target_dir)

print(os.getcwd())


