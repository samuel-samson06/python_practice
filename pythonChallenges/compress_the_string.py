from itertools import groupby
arr = []
test = input()
see = groupby(test)
for i, j in see:
    arr.append(f"({len(tuple(j))}, {i})")
print(" ".join(arr))
