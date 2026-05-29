import os

base_dir = os.getcwd()

target_dir = os.path.join(base_dir,"Concepts","Os_Module")

if os.getcwd() != target_dir:
    os.chdir(target_dir)

# print(os.getcwd())

if not os.path.exists("Experiment"):
    os.mkdir("Experiment")

# for i in range(5):
#     os.mkdir(f"Experiment/Day{i+1}")

# for i in range(5):
#     os.rename(f"Experiment/Test{i+1}" , f"Experiment/Test_{i+1}")

for i in range(5):
    folder_name = f"Experiment/Test_{i+1}"
    file_path = f"{folder_name}/main.py"
    with open(file_path,"w") as file:
        file.write("# A Test Python file\n")


