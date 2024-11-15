length, breadth = input("Values:").split()
length = int(length)
breadth = int(breadth)
# Goes from 1 - length every 2 steps
for i in range(1, length+1, 2):
    char_multiplier = ".|."*i
    if i != length:
        print(char_multiplier.center(breadth, "-"))
print("WELCOME".center(breadth, "-"))
#  The Algorithm works by removing 1 then taking negative steps backward,  run the code to understand with only "i"
for i in range(length-2, -1, -2):
    char_multiplier = ".|."*i
    if i != length:
        print(char_multiplier.center(breadth, "-"))
