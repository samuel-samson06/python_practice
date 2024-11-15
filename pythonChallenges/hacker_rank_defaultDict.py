from collections import defaultdict
default_dict = defaultdict(list)
test_positions  = defaultdict(list)
n, m = list(map(lambda x: int(x), input("Enter N and M::").split(" ")))

for i in range(0,n):
    group_A_input = input("Enter Group A::")
    test_positions[group_A_input].append(str(i+1))
for _ in range(0,m):
    group_B_input = input("Enter Group B::")
    if group_B_input in test_positions:
        print(" ".join(test_positions[group_B_input]))
    else:
        print(-1)
