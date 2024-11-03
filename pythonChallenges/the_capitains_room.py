#Hacker Rank The Captains Room
group_size = int(input("Enter the Group Size::"))
converted_rooms = list(map(lambda x:int(x),input("Enter Room Number::").split(" ")))
print(list(set(converted_rooms))[-1])