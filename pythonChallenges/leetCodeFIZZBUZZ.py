print("WELCOME TO THE FIZZ BUZZ GAME!!!!")

n = 15
arrayOfAnswers = []

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        arrayOfAnswers.append("FizzBuzz")
    elif i % 3 == 0:
        arrayOfAnswers.append("Fizz")
    elif i % 5 == 0:
        arrayOfAnswers.append("Buzz")
    else:
        arrayOfAnswers.append(i)
print(arrayOfAnswers)