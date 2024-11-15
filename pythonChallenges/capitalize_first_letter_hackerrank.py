def solve(s):
    array_test = []
    split_name = s.split(" ")
    for i in split_name:
        if i == "":
            array_test.append(i)
        else:
            capitalized = i[0].upper() + i[1:]
            array_test.append(capitalized)
    return " ".join(array_test)


if __name__ == '__main__':
    word = input()
    result = solve(word)
    print(result)
