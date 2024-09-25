import os

# print(os.getcwd())
# print(os.path.join('test','testing','testing-test'))
# os.makedirs("C:\\Users\\SAMUEL\Desktop\\test_folder\\testFile.txt")
# print(os.makedirs("C:\\Users\\SAMUEL\Desktop\\test_folder\\testFile.py"))
# print(os.path.isabs('.'))
path = os.getcwd()
# print(path)
directory_name = os.path.dirname(path)
# print(directory_name)
# print(path)
# print(os.listdir(path))
trial = (os.listdir(os.path.dirname(path)))
# for i in trial:
#     print(i,os.path.getsize(directory_name+f'\\{i}'))