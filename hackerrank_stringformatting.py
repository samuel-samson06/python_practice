"""So basically the task I'm tackling is to string format
I'll be taking input from a user number to be precise and ill print out the numbers in a tabular format.
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001

   like this
   in order to achieve each of them ill be using the built-in python functions oct() hex() bin()
   My major task is to make the format like the above code example
"""


def print_formatted(number):

    for i in range(number):
        # test = i+1
        # space = len(str(bin(number))[2:])-1
        # print(str(test).rjust(space),str(oct(test)).split("o")[-1].rjust(space),str(hex(test)).split("x")[-1].upper().rjust(space),str(bin(test)).split("b")[
        #     -1].rjust(space))
        n = int(input())
        k = len(bin(n)) - 2 + 1
        for i in range(1, n + 1):
            print(str(i).rjust(k - 1) + oct(i)[2:].upper().rjust(k) + hex(i)[2:].upper().rjust(k) + bin(i)[2:].rjust(k))
        # print(space)
        # print(f"{test} {str(oct(test)).split("o")[-1]} {str(hex(test)).split("x")[-1].upper()} {str(bin(test)).split("b")[-1]}")

user_input = int(input('enter::'))
print_formatted(user_input)
