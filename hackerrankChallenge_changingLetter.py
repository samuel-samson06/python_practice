def mutate_string(string, position, character):
    test = list(string)
    test[position] = character
    return "".join(test)


if __name__ == '__main__':
    s = input("Test:- ")
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
