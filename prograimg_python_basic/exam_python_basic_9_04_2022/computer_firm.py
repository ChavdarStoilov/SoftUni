count_computers = int(input())

count_sales = 0
count_rate = 0

for computer in range(count_computers):

    computers = int(input())
    num_in_str = str(computers)
    last_num = num_in_str[2]
    first_two_num = num_in_str[0:2]

    count_rate += int(last_num)


    if int(last_num) == 2:
        possible_sales = 0
    elif int(last_num) == 3:
        possible_sales = 0.50
    elif int(last_num) == 4:
        possible_sales = 0.70
    elif int(last_num) == 5:
        possible_sales = 0.85
    else:
        possible_sales = 1

    sales = int(first_two_num) * possible_sales
    count_sales += sales

print(f"{count_sales:.2f}")
avg_rate = count_rate / count_computers
print(f"{avg_rate:.2f}")