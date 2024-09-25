scores_int = []
n = input("Enter Number: ")
scores = input("Enter Scores: ").split()
scores.sort(key=int)
turn_set = set(scores)
turn_list = list(turn_set)
for i in turn_list:
    scores_int.append(int(i))
scores_int.sort()
print(str(scores_int[len(scores_int)-2]))
# input()
# numbers = input().split()
# numbers.sort(key=int)
# i = numbers.pop()
# print("This is I", i)
# a = i
# while a == i:
#     a = numbers.pop()
# print(a)
