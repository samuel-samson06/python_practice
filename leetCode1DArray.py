# So Basically this Code Receives a list and add the List together based on the value after it
# Example nums = [3,1,2,10,1]
# output = [3,4,6,16,17]

one_dimensional_array = []

given_array = [3, 1, 2, 10, 1]
increment = 0

for i in given_array:
    increment += i
    one_dimensional_array.append(increment)
print(one_dimensional_array)

