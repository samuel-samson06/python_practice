def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        x = int(input("Enter Number:: "))
        if collatz(x) == 1:
            break
        else:
            continue
    except ValueError:
        print("Print Enter a Number")
        continue
