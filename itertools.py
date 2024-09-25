from itertools import product
A = input().split()
B = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
for i in range(len(B)):
    B[i] = int(B[i])
C = list(product(A, B))

print(*C)