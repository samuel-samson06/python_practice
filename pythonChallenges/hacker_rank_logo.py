user_input = 5
for i in range(5):
    formula = ((i+1)+i)
    # Formula 1 i+1, i
    print(("H"*formula).center(9, " "))
for j in range(6):
    for k in range(25):
        if 7 < k+1 < 20:
            print(" ", end="")
        else:
            print("H", end="")

    print("")
