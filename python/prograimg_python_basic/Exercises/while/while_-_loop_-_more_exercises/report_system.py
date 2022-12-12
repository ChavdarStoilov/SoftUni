sum_collected = int(input())
money = input()

count = 0
count_cs_money = 0
count_cc_money = 0
count_cs = 0
count_cc = 0
end_sum = 0

while money != "End":
    money = int(money)
    count += 1

    if count % 2 == 0:
        if money < 10:
            print("Error in transaction!")
        else:
            count_cc += 1
            count_cc_money += money
            end_sum += money
            print("Product sold!")

    else:
        if money > 100:
            print("Error in transaction!")
        else:
            count_cs += 1
            count_cs_money += money
            end_sum += money
            print("Product sold!")

    if sum_collected <= end_sum:
        break

    money = input()


if sum_collected <= end_sum:
    avg_cs = count_cs_money / count_cs
    avg_cc = count_cc_money / count_cc
    print(f"Average CS: {avg_cs:.2f}\n"
          f"Average CC: {avg_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
