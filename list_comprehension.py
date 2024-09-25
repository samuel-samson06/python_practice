res = []

x = 2
y = 2
z = 2
n = 2

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(z+1):
            if sum([i, j, k]) != n:
                res.append([i, j, k])
print(res)
