consecutiveList = []

n = int(input("Enter Number:: "))
for i in range(n):
    consecutiveList.append(str(i+1))
print(''.join(consecutiveList))