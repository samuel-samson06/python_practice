amount_to_run = int(input())
records = []
scores = []
student_lowest_score = []
for names in range(0, amount_to_run):
    name = input('')
    number = float(input(""))
    records.append([name, number])

for i, j in records:
    scores.append(j)
transform_to_set = set(scores)
to_list = list(transform_to_set)
to_list.sort()
second_lowest = to_list[1]
for students in records:
    if students[1] == second_lowest:
        student_lowest_score.append(students[0])

student_lowest_score.sort()
for student in student_lowest_score:
    print(student)
