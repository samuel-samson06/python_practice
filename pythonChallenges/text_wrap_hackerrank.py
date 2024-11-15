def wrap(user_string, user_max_width):
    test_array = []
    length_string = len(user_string)
    for i in range(0, length_string, user_max_width):
        test_calculation = i + user_max_width
        test_array.append(string[i:test_calculation])
    return "\n".join(test_array)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
