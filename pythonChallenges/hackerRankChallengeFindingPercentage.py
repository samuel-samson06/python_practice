amount_of_times_to_run = int(input("How many People's test:- "))
student_array = []

for i in range(amount_of_times_to_run):
    student = input("Enter student name and scores:- ").split()
    score_addition = 0
    for j in student[1:]:
        score_addition += float(j)
    average_score = score_addition/3
    formatted = f"{average_score:.2f}"
    student_array.append({"name": student[0], "score": formatted})

student_name = input("Enter Student Name:- ")
for students in student_array:
    if student_name == students["name"]:
        print(students["score"])
