# def print_rangoli(size):
#     h = (size - 1) * 2 +1                           #height
#     w = (h - 1) * 2 +1                              #width
#     fin = ""
#     for row_number in range(1, size + 1):           #upper + middle
#         symbols = []
#         for col in range(row_number):               #left part of row
#             symbols += chr(96 + (size - col))
#         for col in range(row_number - 1, 0, -1):    #right part of row
#             symbols += chr(97 + size - col)
#         s = "-".join(symbols)
#         fin += f"{s:-^{w}}\n"
#     for row_number in range(size - 1, 0, -1):       #lower
#         symbols = []
#         for col in range(row_number):               #left part of row
#             symbols += chr(96 + (size - col))
#         for col in range(row_number - 1, 0, -1):    #right part of row
#             symbols += chr(97 + size - col)
#         s = "-".join(symbols)
#         fin += f"{s:-^{w}}\n"
#     print(fin)
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


user_number = 3
alphabet = [chr(i) for i in range(97, 123)]
alphabet = alphabet[:user_number]
list_char = list(range(user_number))
reversed_list = list_char[:-1]+list_char[::-1]
for i in reversed_list:
    start_index = i + 1
    original = alphabet[-start_index:]
    reverse = original[::-1]
    row = reverse+original[1:]
    row = "-".join(row)
    width = user_number*4 - 3
    row = row.center(width ,  "-")
    print(row)
