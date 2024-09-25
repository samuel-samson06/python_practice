from collections import Counter

amount_shoes_available = int(input(""))
enter_sizes = input("").split()
amount_customers = int(input(""))
counter = Counter(enter_sizes)
total_sales_list = []
for i in range(amount_customers):
    customer = input("").split()
    if customer[0] in counter.keys() and counter[customer[0]] > 0:
        counter[customer[0]] -= 1
        total_sales_list.append(customer[1])
total_sales = 0
for i in total_sales_list:
    total_sales += int(i)
print(total_sales)
