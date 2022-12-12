months = int(input())

bill_for_water = 20 * months
bill_for_internet = 15 * months
bill_for_current = 0

for bills in range(months):
    bill_for_current_per_months = float(input())
    bill_for_current += bill_for_current_per_months



the_others =(bill_for_water + (bill_for_water * 0.20))+ (bill_for_internet + (bill_for_internet * 0.20)) \
            + bill_for_current + (bill_for_current * 0.20)
sum = bill_for_water + bill_for_internet + bill_for_current + the_others
avg = sum / months

print(f"Electricity: {bill_for_current:.2f} lv\n"
      f"Water: {bill_for_water:.2f} lv\n"
      f"Internet: {bill_for_internet:.2f} lv\n"
      f"Other: {the_others:.2f} lv\n"
      f"Average: {avg:.2f} lv")