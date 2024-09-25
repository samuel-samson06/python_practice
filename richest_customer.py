account = [[7, 1, 3], [2, 8, 7], [1, 9, 5]]

general_sum = []

for i in account:
    sum_of_i = sum(i)
    general_sum.append(sum_of_i)
print(f"The Richest Customer is {max(general_sum)}")
