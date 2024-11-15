def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        split_int_k = string[i:i + k]
        test_list = []
        for j in split_int_k:
            if j in test_list:
                ...
            else:
                test_list.append(j)
        print("".join(test_list))

if __name__ == "__main__":
    string, k = input("string::"), int(input("k::"))
    merge_the_tools(string, k)

# PSEUDO CODE TO SOLVE PROBLEM
# string = "ABRACADABRA"
# k = 3
# merge_list = []
# if len(string) % k != 0:
#     print("Cant run")
# else:
#     for i in range(0, len(string), k):
#         split_int_k = string[i:i+k]
#         # print(split_int_k)
#         test_list = []
#         for j in split_int_k:
#             if j in test_list:
#                 ...
#             else:
#                 test_list.append(j)
#         print("".join(test_list))
