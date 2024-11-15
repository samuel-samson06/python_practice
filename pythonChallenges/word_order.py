from collections import Counter
list_of_inputs = []
list_len = []
list_amount = []
number_input = int(input("Enter Input::"))
for i in range(0, number_input):
    user_input = input("Enter Word::")
    list_of_inputs.append(user_input)
test_aga = Counter(list_of_inputs)
print(test_aga)
for key, value in test_aga.items():
    list_len.append(value)
    list_amount.append(str(value))
print(len(list_len))
print(" ".join(list_amount))
