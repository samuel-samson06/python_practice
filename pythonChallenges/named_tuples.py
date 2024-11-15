from collections import namedtuple
number_students = int(input("Number of Student:::"))
columns = input("Enter Columns:::")
students  = namedtuple("Students",columns.split(" "))
total = 0
for i in range(number_students):
    test = input("First Student:::").split(" ")
    testing = students(*test)
    total+=int(testing.MARKS)
print(f"{total / number_students:.2f}")
