def average(array):
    set_array = set(array)
    list_set = list(set_array)
    average_list = sum(list_set)/len(list_set)
    return average_list


print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))
