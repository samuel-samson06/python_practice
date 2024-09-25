happy = 0
n, m = input(":::").split()
arr = list(map(lambda x: int(x), input("arr:::").split()))
A = set(map(lambda x: int(x), input("A:::").split()))
B = set(map(lambda x: int(x), input("B:::").split()))
for i in arr:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print(happy)

