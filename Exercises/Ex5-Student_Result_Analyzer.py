
marks_dict = {
    "Rahul" : [78,89,90],
    "Priya" : [92,85,88],
    "Arjun" : [67,72,70]
}

marks_list = [i for i in marks_dict.values()]

avg_marks = [(sum(i)/len(i)) for i in marks_list]

if avg_marks[0] > avg_marks[1]:
    if avg_marks[0] > avg_marks[2]:
        print(f"Rahul is the Topper with an average maarks of {avg_marks[0]}\n")
    else:
        print(f"Arjun is the Topper with an average maarks of {avg_marks[2]}\n")
else:
    if avg_marks[1] > avg_marks[2]:
        print(f"Priya is the Topper with an average maarks of {avg_marks[1]}\n")
    else:
        print(f"Arjun is the Topper with an average maarks of {avg_marks[2]}\n")

names_list = [i for i in marks_dict.keys()]

for i in range(len(names_list)):
    print(f"{names_list[i]} scored : {marks_list[i]}\n")

cl_avg = sum(avg_marks)/len(avg_marks)
print(f"Class avg is {cl_avg}")