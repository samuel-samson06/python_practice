def swap_case(parameter):
    array_swap = []

    for i in parameter:
        if i.isupper():
            array_swap.append(i.lower())
        elif i.islower():
            array_swap.append(i.upper())
        else:
            array_swap.append(i)
    return "".join(array_swap)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
