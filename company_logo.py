from collections import Counter

s = input()
company_name_list = []
for i in s:
    company_name_list.append(i)
result = Counter(sorted(company_name_list)).most_common(3)
for letter, count in result:
    print(letter, count)