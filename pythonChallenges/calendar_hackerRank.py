import calendar
user_input = "08 05 2015".split()
convert = list(map(lambda x: int(x), user_input))
array_days = days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(array_days[calendar.weekday(convert[2], convert[0], convert[1])].upper())
