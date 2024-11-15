n = 20
counter = 0

while n > 1:
    if n % 2 == 0:
        n /= 2
        counter += 1
    else:
        n -= 1
        counter += 1

if counter > 0:
    print(counter+1)
else:
    print(counter)
