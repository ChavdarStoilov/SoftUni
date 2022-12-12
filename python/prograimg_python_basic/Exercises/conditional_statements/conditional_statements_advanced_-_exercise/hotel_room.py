months = str(input())
days = int(input())

studio = 0
apartment = 0
discount = 0
end_sum = 0
discount_studio = 0

if months == "May" or months == "October":
    studio = 50
    apartment = 65

    if 7 < days < 14:
        discount_studio = (studio * days) * 0.05
    elif days > 14:
        discount_studio = (studio * days) * 0.30

elif months == "June" or months == "September":
    studio = 75.20
    apartment = 68.70

    if days > 14:
        discount_studio = (studio * days) * 0.20

elif months == "July" or months == "August":
    studio = 76
    apartment = 77


if days > 14:
    discount = (apartment * days) * 0.10
    apartment = (apartment * days) - discount

else:
    apartment = apartment * days

end_sum = (studio * days) - discount_studio

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {end_sum:.2f} lv.")