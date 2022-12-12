bonus = float()
points = int(input())

if points <= 100:
    bonus = 5

elif points > 1000:
    bonus = points * 0.10

else:
    bonus = points * 0.20

if points % 2 == 0:
    bonus = bonus + 1

elif points % 10 == 5:
    bonus = bonus + 2

print(bonus)
print(points + bonus)