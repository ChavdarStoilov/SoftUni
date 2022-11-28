count = int(input())

minibus = 0
truck = 0
train = 0
price = 0
count_tone = 0

for tones in range(count):
    tone = int(input())
    count_tone += tone

    if tone <= 3:
        price += tone * 200
        minibus += tone

    elif 11 >= tone >= 4:
        price += tone * 175
        truck += tone

    else:
        price += tone * 120
        train += tone


avg = price / count_tone
prec_minibus = (minibus / count_tone) * 100
prec_truck = (truck / count_tone) * 100
prec_train = (train / count_tone) * 100

print(f"{avg:.2f}")
print(f"{prec_minibus:.2f}%")
print(f"{prec_truck:.2f}%")
print(f"{prec_train:.2f}%")


