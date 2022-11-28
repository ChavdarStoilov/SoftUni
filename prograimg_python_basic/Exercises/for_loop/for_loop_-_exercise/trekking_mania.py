count_of_group_people = int(input())

count_people = 0
musala = 0
monblan = 0
kalimadgaro = 0
k_two = 0
everest = 0

for people in range(count_of_group_people):
    people_in_group = int(input())

    count_people += people_in_group

    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kalimadgaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k_two += people_in_group
    else:
        everest += people_in_group

musala_percentage = (musala / count_people) * 100
monblan_percentage = (monblan / count_people) * 100
kalimadgaro_percentage = (kalimadgaro / count_people) * 100
k_two_percentage = (k_two / count_people) * 100
everest_percentage = (everest / count_people) * 100

print(f"{musala_percentage:.2f}% \n{monblan_percentage:.2f}% \n{kalimadgaro_percentage:.2f}%"
      f" \n{k_two_percentage:.2f}% \n{everest_percentage:.2f}%")