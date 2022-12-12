capacity_of_stadium = int(input())
count_of_fan = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for sectors in range(count_of_fan):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    else:
        sector_g += 1


perg_sector_a = (sector_a / count_of_fan) * 100
perg_sector_b = (sector_b / count_of_fan) * 100
perg_sector_v = (sector_v / count_of_fan) * 100
perg_sector_g = (sector_g / count_of_fan) * 100
perg_count_of_fan = (count_of_fan / capacity_of_stadium) * 100

print(f"{perg_sector_a:.2f}%\n"
      f"{perg_sector_b:.2f}%\n"
      f"{perg_sector_v:.2f}%\n"
      f"{perg_sector_g:.2f}%\n"
      f"{perg_count_of_fan:.2f}%")