general_list = []
user_list = []
times_to_run = int(input(""))
for i in range(times_to_run):
    user_input = input("").strip().split()
    if 'insert' in user_input:
        test = user_input
        user_list.insert(int(user_input[1]), int(user_input[2]))
    elif 'print' in user_input:
        general_list.append(tuple(user_list))
    elif 'remove' in user_input:
        user_list.remove(int(user_input[1]))
    elif 'append' in user_input:
        user_list.append(int(user_input[1]))
    elif 'sort' in user_input:
        user_list.sort()
    elif 'pop' in user_input:
        user_list.pop()
    elif 'reverse' in user_input:
        user_list.reverse()
for all_list in general_list:
    print(list(all_list))